namespace CareEvolution.Orchestrate;

internal static class TranslateFhirR4ConceptMapParametersBuilder
{
    public static Parameters Build(TranslateFhirR4ConceptMapRequest request)
    {
        var coding = new Coding
        {
            System = string.IsNullOrEmpty(request.System) ? null : request.System,
            Code = string.IsNullOrEmpty(request.Code) ? null : request.Code,
            Display = string.IsNullOrEmpty(request.Display) ? null : request.Display,
        };

        var parameter = new List<Parameters.ParameterComponent>();
        if (!string.IsNullOrEmpty(request.Domain))
        {
            parameter.Add(
                new Parameters.ParameterComponent
                {
                    Name = "domain",
                    Value = new Hl7.Fhir.Model.FhirString(request.Domain),
                }
            );
        }
        parameter.Add(new Parameters.ParameterComponent { Name = "coding", Value = coding });

        return new Parameters { Parameter = parameter };
    }
}
