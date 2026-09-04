using Hl7.Fhir.Model;

namespace CareEvolution.Orchestrate.Tests;

public sealed class TranslateFhirR4ConceptMapParametersBuilderTests
{
    [Fact]
    public void BuildShouldSendOnlyCodeWhenNothingElseGiven()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest { Code = "119981000146107" }
        );

        var coding = Assert.Single(parameters.Parameter);
        Assert.Equal("coding", coding.Name);
        var value = Assert.IsType<Coding>(coding.Value);
        Assert.Equal("119981000146107", value.Code);
        Assert.Null(value.System);
        Assert.Null(value.Display);
    }

    [Fact]
    public void BuildShouldAddDomainParameterWhenDomainGiven()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest
            {
                Code = "119981000146107",
                Domain = TranslateDomains.DiagnosisCode,
            }
        );

        Assert.Collection(
            parameters.Parameter,
            p => Assert.Equal("domain", p.Name),
            p => Assert.Equal("coding", p.Name)
        );
        var domain = parameters.Parameter[0];
        Assert.Equal(TranslateDomains.DiagnosisCode, ((FhirString)domain.Value!).Value);
    }

    [Fact]
    public void BuildShouldCarrySystemAndDisplayIntoCoding()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest
            {
                Code = "119981000146107",
                System = "http://snomed.info/sct",
                Display = "Essential hypertension",
            }
        );

        var coding = (Coding)parameters.Parameter.Single(p => p.Name == "coding").Value!;
        Assert.Equal("http://snomed.info/sct", coding.System);
        Assert.Equal("119981000146107", coding.Code);
        Assert.Equal("Essential hypertension", coding.Display);
    }

    [Fact]
    public void BuildShouldAllowDisplayWithoutCode()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest { Display = "Essential hypertension" }
        );

        var coding = (Coding)parameters.Parameter.Single(p => p.Name == "coding").Value!;
        Assert.Null(coding.Code);
        Assert.Equal("Essential hypertension", coding.Display);
    }

    [Fact]
    public void BuildShouldDropEmptyFields()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest { Code = "119981000146107", System = "" }
        );

        var coding = (Coding)parameters.Parameter.Single(p => p.Name == "coding").Value!;
        Assert.Null(coding.System);
        Assert.Equal("119981000146107", coding.Code);
    }

    [Fact]
    public void BuildShouldTreatWhitespaceOnlyFieldsAsAbsent()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest { Code = "119981000146107", System = "   " }
        );

        var coding = (Coding)parameters.Parameter.Single(p => p.Name == "coding").Value!;
        Assert.Null(coding.System);
        Assert.Equal("119981000146107", coding.Code);
    }

    [Fact]
    public void BuildShouldOmitDomainParameterWhenDomainIsWhitespaceOnly()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest { Code = "119981000146107", Domain = "   " }
        );

        var coding = Assert.Single(parameters.Parameter);
        Assert.Equal("coding", coding.Name);
    }

    [Fact]
    public void BuildShouldOmitCodingParameterWhenAllCodingFieldsAreAbsent()
    {
        var parameters = TranslateFhirR4ConceptMapParametersBuilder.Build(
            new TranslateFhirR4ConceptMapRequest { System = "  " }
        );

        Assert.Empty(parameters.Parameter);
    }
}
