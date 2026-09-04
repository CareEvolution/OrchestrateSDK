namespace CareEvolution.Orchestrate;

internal static class TranslateFhirR4ConceptMapParametersBuilder
{
    public static Parameters Build(TranslateFhirR4ConceptMapRequest request)
    {
        var coding = new Coding
        {
            System = string.IsNullOrWhiteSpace(request.System) ? null : request.System,
            Code = string.IsNullOrWhiteSpace(request.Code) ? null : request.Code,
            Display = string.IsNullOrWhiteSpace(request.Display) ? null : request.Display,
        };

        var parameter = new List<Parameters.ParameterComponent>();
        if (!string.IsNullOrWhiteSpace(request.Domain))
        {
            parameter.Add(
                new Parameters.ParameterComponent
                {
                    Name = "domain",
                    Value = new Hl7.Fhir.Model.FhirString(request.Domain),
                }
            );
        }
        if (coding.System != null || coding.Code != null || coding.Display != null)
        {
            parameter.Add(new Parameters.ParameterComponent { Name = "coding", Value = coding });
        }

        return new Parameters { Parameter = parameter };
    }
}
