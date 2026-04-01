using System.IO.Compression;
using CareEvolution.Orchestrate.Exceptions;
using CareEvolution.Orchestrate.Tests.Helpers;

namespace CareEvolution.Orchestrate.Tests;

public sealed class LiveApiTests : IDisposable
{
    private static readonly byte[] PdfMagicNumber = [37, 80, 68, 70];
    private static readonly byte[] PkZipMagicNumber = [80, 75, 3, 4];
    private readonly HttpClient _httpClient = new();
    private readonly OrchestrateApi _api;
    private static readonly ClassifyConditionRequest[] ClassifyConditionRequestItems =
    [
        new ClassifyConditionRequest
        {
            Code = "119981000146107",
            System = "http://snomed.info/sct",
        },
        new ClassifyConditionRequest { Code = "119981000146107", System = "SNOMED" },
    ];
    private static readonly ClassifyMedicationRequest[] ClassifyMedicationRequestItems =
    [
        new ClassifyMedicationRequest
        {
            Code = "2468231",
            System = "http://www.nlm.nih.gov/research/umls/rxnorm",
        },
        new ClassifyMedicationRequest { Code = "2468231", System = "RxNorm" },
    ];
    private static readonly ClassifyObservationRequest[] ClassifyObservationRequestItems =
    [
        new ClassifyObservationRequest { Code = "94558-4", System = "http://loinc.org" },
        new ClassifyObservationRequest { Code = "94558-4", System = "LOINC" },
    ];
    private static readonly (
        StandardizeRequest Request,
        string ExpectedCode
    )[] StandardizeConditionCases =
    [
        (new StandardizeRequest { Code = "370221004" }, "370221004"),
        (new StandardizeRequest { Code = "J45.50" }, "J45.50"),
        (new StandardizeRequest { Display = "dm2" }, "44054006"),
    ];
    private static readonly (
        StandardizeRequest Request,
        string ExpectedCode
    )[] StandardizeLabCases =
    [
        (new StandardizeRequest { Code = "4548-4" }, "4548-4"),
        (new StandardizeRequest { Display = "hba1c 1/15/22 from outside lab" }, "43396009"),
    ];
    private static readonly (
        StandardizeRequest Request,
        string ExpectedCode
    )[] StandardizeMedicationCases =
    [
        (new StandardizeRequest { Code = "861004", System = "RxNorm" }, "861004"),
        (new StandardizeRequest { Code = "59267-1000-02" }, "59267100002"),
        (
            new StandardizeRequest
            {
                Display = "Jentadueto extended (linagliptin 2.5 / metFORMIN  1000mg)",
            },
            "1796093"
        ),
    ];
    private static readonly (
        StandardizeRequest Request,
        string ExpectedCode
    )[] StandardizeObservationCases =
    [
        (new StandardizeRequest { Code = "8480-6" }, "8480-6"),
        (new StandardizeRequest { Display = "BMI" }, "39156-5"),
    ];
    private static readonly (
        StandardizeRequest Request,
        string ExpectedCode
    )[] StandardizeProcedureCases =
    [
        (new StandardizeRequest { Code = "80146002" }, "80146002"),
        (new StandardizeRequest { Display = "ct head&neck" }, "429858000"),
    ];
    private static readonly (
        StandardizeRequest Request,
        string ExpectedCode
    )[] StandardizeRadiologyCases =
    [
        (new StandardizeRequest { Code = "711232001", System = "SNOMED" }, "711232001"),
        (
            new StandardizeRequest { Display = "CT scan of head w/o iv contrast 3d ago@StJoes" },
            "30799-1"
        ),
    ];

    public static TheoryData<ClassifyConditionRequest> ClassifyConditionRequests =>
        new() { ClassifyConditionRequestItems[0], ClassifyConditionRequestItems[1] };

    public static TheoryData<ClassifyMedicationRequest> ClassifyMedicationRequests =>
        new() { ClassifyMedicationRequestItems[0], ClassifyMedicationRequestItems[1] };

    public static TheoryData<ClassifyObservationRequest> ClassifyObservationRequests =>
        new() { ClassifyObservationRequestItems[0], ClassifyObservationRequestItems[1] };

    public static TheoryData<StandardizeRequest, string> StandardizeConditionRequests =>
        new()
        {
            { StandardizeConditionCases[0].Request, StandardizeConditionCases[0].ExpectedCode },
            { StandardizeConditionCases[1].Request, StandardizeConditionCases[1].ExpectedCode },
            { StandardizeConditionCases[2].Request, StandardizeConditionCases[2].ExpectedCode },
        };

    public static TheoryData<StandardizeRequest, string> StandardizeLabRequests =>
        new()
        {
            { StandardizeLabCases[0].Request, StandardizeLabCases[0].ExpectedCode },
            { StandardizeLabCases[1].Request, StandardizeLabCases[1].ExpectedCode },
        };

    public static TheoryData<StandardizeRequest, string> StandardizeMedicationRequests =>
        new()
        {
            { StandardizeMedicationCases[0].Request, StandardizeMedicationCases[0].ExpectedCode },
            { StandardizeMedicationCases[1].Request, StandardizeMedicationCases[1].ExpectedCode },
            { StandardizeMedicationCases[2].Request, StandardizeMedicationCases[2].ExpectedCode },
        };

    public static TheoryData<StandardizeRequest, string> StandardizeObservationRequests =>
        new()
        {
            { StandardizeObservationCases[0].Request, StandardizeObservationCases[0].ExpectedCode },
            { StandardizeObservationCases[1].Request, StandardizeObservationCases[1].ExpectedCode },
        };

    public static TheoryData<StandardizeRequest, string> StandardizeProcedureRequests =>
        new()
        {
            { StandardizeProcedureCases[0].Request, StandardizeProcedureCases[0].ExpectedCode },
            { StandardizeProcedureCases[1].Request, StandardizeProcedureCases[1].ExpectedCode },
        };

    public static TheoryData<StandardizeRequest, string> StandardizeRadiologyRequests =>
        new()
        {
            { StandardizeRadiologyCases[0].Request, StandardizeRadiologyCases[0].ExpectedCode },
            { StandardizeRadiologyCases[1].Request, StandardizeRadiologyCases[1].ExpectedCode },
        };

    public LiveApiTests()
    {
        _api = LiveClients.CreateOrchestrateApi(_httpClient);
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(ClassifyConditionRequests))]
    public async Task ClassifyConditionShouldClassifySingleRequest(ClassifyConditionRequest request)
    {
        var result = await _api.Terminology.ClassifyConditionAsync(request);
        Assert.NotNull(result);
        Assert.True(result.CciAcute);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ClassifyConditionShouldClassifyBatch()
    {
        var results = await _api.Terminology.ClassifyConditionAsync(ClassifyConditionRequestItems);
        Assert.Equal(2, results.Count);
        Assert.All(results, result => Assert.True(result.CciAcute));
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(ClassifyMedicationRequests))]
    public async Task ClassifyMedicationShouldClassifySingleRequest(
        ClassifyMedicationRequest request
    )
    {
        var result = await _api.Terminology.ClassifyMedicationAsync(request);
        Assert.True(result.RxNormGeneric);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ClassifyMedicationShouldClassifyBatch()
    {
        var results = await _api.Terminology.ClassifyMedicationAsync(
            ClassifyMedicationRequestItems
        );
        Assert.Equal(2, results.Count);
        Assert.All(results, result => Assert.True(result.RxNormGeneric));
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(ClassifyObservationRequests))]
    public async Task ClassifyObservationShouldClassifySingleRequest(
        ClassifyObservationRequest request
    )
    {
        var result = await _api.Terminology.ClassifyObservationAsync(request);
        Assert.Equal("MICRO", result.LoincClass);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ClassifyObservationShouldClassifyBatch()
    {
        var results = await _api.Terminology.ClassifyObservationAsync(
            ClassifyObservationRequestItems
        );
        Assert.Equal(2, results.Count);
        Assert.All(results, result => Assert.Equal("MICRO", result.LoincClass));
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(StandardizeConditionRequests))]
    public async Task StandardizeConditionShouldStandardizeSingleRequest(
        StandardizeRequest request,
        string expectedCode
    )
    {
        var result = await _api.Terminology.StandardizeConditionAsync(request);
        Assert.Contains(result.Coding, coding => coding.Code == expectedCode);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeConditionShouldStandardizeBatch()
    {
        var requests = StandardizeConditionCases.Select(row => row.Request).ToList();
        var expected = StandardizeConditionCases.Select(row => row.ExpectedCode).ToList();
        var results = await _api.Terminology.StandardizeConditionAsync(requests);
        Assert.Equal(3, results.Count);
        for (var index = 0; index < results.Count; index++)
        {
            Assert.Contains(results[index].Coding, coding => coding.Code == expected[index]);
        }
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(StandardizeLabRequests))]
    public async Task StandardizeLabShouldStandardizeSingleRequest(
        StandardizeRequest request,
        string expectedCode
    )
    {
        var result = await _api.Terminology.StandardizeLabAsync(request);
        Assert.Contains(result.Coding, coding => coding.Code == expectedCode);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeLabShouldStandardizeBatch()
    {
        var requests = StandardizeLabCases.Select(row => row.Request).ToList();
        var expected = StandardizeLabCases.Select(row => row.ExpectedCode).ToList();
        var results = await _api.Terminology.StandardizeLabAsync(requests);
        Assert.Equal(2, results.Count);
        for (var index = 0; index < results.Count; index++)
        {
            Assert.Contains(results[index].Coding, coding => coding.Code == expected[index]);
        }
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(StandardizeMedicationRequests))]
    public async Task StandardizeMedicationShouldStandardizeSingleRequest(
        StandardizeRequest request,
        string expectedCode
    )
    {
        var result = await _api.Terminology.StandardizeMedicationAsync(request);
        Assert.Contains(result.Coding, coding => coding.Code == expectedCode);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeMedicationShouldStandardizeBatch()
    {
        var requests = StandardizeMedicationCases.Select(row => row.Request).ToList();
        var expected = StandardizeMedicationCases.Select(row => row.ExpectedCode).ToList();
        var results = await _api.Terminology.StandardizeMedicationAsync(requests);
        Assert.Equal(3, results.Count);
        for (var index = 0; index < results.Count; index++)
        {
            Assert.Contains(results[index].Coding, coding => coding.Code == expected[index]);
        }
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(StandardizeObservationRequests))]
    public async Task StandardizeObservationShouldStandardizeSingleRequest(
        StandardizeRequest request,
        string expectedCode
    )
    {
        var result = await _api.Terminology.StandardizeObservationAsync(request);
        Assert.Contains(result.Coding, coding => coding.Code == expectedCode);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeObservationShouldStandardizeBatch()
    {
        var requests = StandardizeObservationCases.Select(row => row.Request).ToList();
        var expected = StandardizeObservationCases.Select(row => row.ExpectedCode).ToList();
        var results = await _api.Terminology.StandardizeObservationAsync(requests);
        Assert.Equal(2, results.Count);
        for (var index = 0; index < results.Count; index++)
        {
            Assert.Contains(results[index].Coding, coding => coding.Code == expected[index]);
        }
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(StandardizeProcedureRequests))]
    public async Task StandardizeProcedureShouldStandardizeSingleRequest(
        StandardizeRequest request,
        string expectedCode
    )
    {
        var result = await _api.Terminology.StandardizeProcedureAsync(request);
        Assert.Contains(result.Coding, coding => coding.Code == expectedCode);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeProcedureShouldStandardizeBatch()
    {
        var requests = StandardizeProcedureCases.Select(row => row.Request).ToList();
        var expected = StandardizeProcedureCases.Select(row => row.ExpectedCode).ToList();
        var results = await _api.Terminology.StandardizeProcedureAsync(requests);
        Assert.Equal(2, results.Count);
        for (var index = 0; index < results.Count; index++)
        {
            Assert.Contains(results[index].Coding, coding => coding.Code == expected[index]);
        }
    }

    [LiveTheory(LiveTestEnvironment.OrchestrateApiKey)]
    [MemberData(nameof(StandardizeRadiologyRequests))]
    public async Task StandardizeRadiologyShouldStandardizeSingleRequest(
        StandardizeRequest request,
        string expectedCode
    )
    {
        var result = await _api.Terminology.StandardizeRadiologyAsync(request);
        Assert.Contains(result.Coding, coding => coding.Code == expectedCode);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeRadiologyShouldStandardizeBatch()
    {
        var requests = StandardizeRadiologyCases.Select(row => row.Request).ToList();
        var expected = StandardizeRadiologyCases.Select(row => row.ExpectedCode).ToList();
        var results = await _api.Terminology.StandardizeRadiologyAsync(requests);
        Assert.Equal(2, results.Count);
        for (var index = 0; index < results.Count; index++)
        {
            Assert.Contains(results[index].Coding, coding => coding.Code == expected[index]);
        }
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task StandardizeBundleShouldStandardize()
    {
        var result = await _api.Terminology.StandardizeBundleAsync(LiveTestData.R4Bundle);
        Assert.NotNull(result.Entry);
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithoutPatientShouldConvert()
    {
        var result = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = LiveTestData.Hl7 }
        );
        Assert.NotNull(result.Entry);
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithPatientShouldConvert()
    {
        var result = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = LiveTestData.Hl7, PatientId = "12/34" }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.Equal("12/34", patient.Id);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithPatientIdentifierAndSystemShouldConvert()
    {
        var result = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request
            {
                Content = LiveTestData.Hl7,
                PatientIdentifier = "1234",
                PatientIdentifierSystem = "GoodHealthClinic",
            }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.True(
            patient.Identifier?.Count > 0
                && patient.Identifier[0].Use == "usual"
                && patient
                    .Identifier[0]
                    .System?.Contains("GoodHealthClinic", StringComparison.Ordinal) == true
                && patient.Identifier[0].Value == "1234"
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithTimezoneShouldConvert()
    {
        var result = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = LiveTestData.Hl7, Tz = "America/New_York" }
        );
        var encounter = GetEntryResourceByType<Hl7.Fhir.Model.R4.Encounter>(
            result,
            Hl7.Fhir.Model.ResourceType.Encounter
        );
        Assert.Equal("2014-11-07T14:40:00-05:00", encounter.Period?.Start);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithoutTimezoneShouldPresumeUtc()
    {
        var result = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = LiveTestData.Hl7 }
        );
        var encounter = GetEntryResourceByType<Hl7.Fhir.Model.R4.Encounter>(
            result,
            Hl7.Fhir.Model.ResourceType.Encounter
        );
        Assert.Equal("2014-11-07T14:40:00+00:00", encounter.Period?.Start);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithLabProcessingHintShouldConvert()
    {
        const string content = """
            MSH|^~\&|||||20220309050000||ORU^R01|||2.7
            PID|1||123456||LastName^FirstName|||||||||||||5678
            PV1|1|I||||||||||||||||||||||||||||||||||||||||||20220309050000
            OBR||001CCK612||ABC^AUTOMATED BLOOD COUNT^LAB|||20220309134200|||2222^ORDERED,BY||||20220309134400|Specimen^|10341^Doctor MD^First^F||||W2622||||HE|F|CBC^ABC|^^^^^R|^~^~^|||||||
            NTE|||Lab Report Comment
            OBX|1|ST|^WBC^LAB|1|1.4|K/UL|4.5-11.5|L^LL|||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|2|ST|^RBC^LAB|1|3.50|M/UL|4.3-5.9|L|||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|3|ST|^HGB^LAB|1|11.6|GM/DL|13.9-16.3|L|||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|4|ST|^HCT^LAB|1|33.7|%|39-55|L|||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|5|ST|^MCV^LAB|1|96.4|FL|80-100||||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|6|ST|^MCH^LAB|1|33.1|PG|25.4-34.6||||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|7|ST|^MCHC^LAB|1|34.3|GM/DL|30-37||||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|8|ST|^RDW^LAB|1|17.9|%|11.5-14.5|H|||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            OBX|9|ST|^PLATELETS^LAB|1|125|K/UL|130-400|L|||F|||202203091347|R^ROUTINE LAB|2222^ORDERED,BY|
            """;

        var hintedResult = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = content, ProcessingHint = "lab" }
        );
        var unhintedResult = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = content }
        );
        var defaultResult = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = content, ProcessingHint = "default" }
        );

        Assert.Equal(9, CountResources(hintedResult, Hl7.Fhir.Model.ResourceType.Observation));
        Assert.Equal(0, CountResources(unhintedResult, Hl7.Fhir.Model.ResourceType.Observation));
        Assert.Equal(0, CountResources(defaultResult, Hl7.Fhir.Model.ResourceType.Observation));
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertHl7ToFhirR4WithTranscriptionProcessingHintShouldConvert()
    {
        const string content = """
            MSH|^~\&||TX|||20110706100000||ORU^R01|||2.3
            PID|1||123456||LastName^FirstName||20000101|M||||||||||7890
            PV1|1|I||||||||||||||||||||||||||||||||||||||||||20110706100000
            ORC|RE|^SCM|||||||20110706100000|||010400^DOE MD^JOHN^^^^
            OBR|1|^SCM|001XYZ555^SCM|CH9^CHEST SPECIAL VIEWS|||20110706100000|||||||20110706100000||010400^DOE MD^JOHN^^^^|||||||||P||^^^20110706100000^^R|~~~~||||010400^DOE MD^JOHN|~|^UNKNOWN^TECHNOLOGIST^^^^|010400^DOE MD^JOHN^^^^
            OBX|1|ST|&GDT^^GDT||Line 1||||||F
            OBX|2|ST|&GDT^Label^GDT||Line 2||||||F
            OBX|3|ST|&GDT^&Not a Label^GDT||Line 3||||||F
            OBX|4|ST|Dictation TS|2|Dictated by: Tue Mar 18, 2025  1:06:45 PM EDT [INTERFACE, INCOMING RADIANT IMAGE AVAILABILITY]||||||Final|||||E175762^MILLER^AMANDA^^^^^^PROVID^^^^PROVID^^^^^^^^RT|||||||||
            """;

        var hintedResult = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = content, ProcessingHint = "transcription" }
        );
        var unhintedResult = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = content }
        );
        var defaultResult = await _api.Convert.Hl7ToFhirR4Async(
            new ConvertHl7ToFhirR4Request { Content = content, ProcessingHint = "default" }
        );

        Assert.Equal(1, CountResources(hintedResult, Hl7.Fhir.Model.ResourceType.Binary));
        Assert.Equal(0, CountResources(unhintedResult, Hl7.Fhir.Model.ResourceType.Binary));
        Assert.Equal(0, CountResources(defaultResult, Hl7.Fhir.Model.ResourceType.Binary));
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToFhirR4WithoutPatientShouldConvert()
    {
        var result = await _api.Convert.CdaToFhirR4Async(
            new ConvertCdaToFhirR4Request { Content = LiveTestData.Cda }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToFhirR4WithIncludeOriginalCdaShouldConvert()
    {
        var result = await _api.Convert.CdaToFhirR4Async(
            new ConvertCdaToFhirR4Request { Content = LiveTestData.Cda, IncludeOriginalCda = true }
        );
        Assert.Contains(
            result.Entry,
            entry =>
                entry.Resource?.ResourceType == Hl7.Fhir.Model.ResourceType.DocumentReference
                && entry.Resource is Hl7.Fhir.Model.R4.DocumentReference doc
                && doc.Type?.Coding?.Any(coding => coding.Code == "Cda") == true
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToFhirR4WithIncludeStandardizedCdaShouldConvert()
    {
        var result = await _api.Convert.CdaToFhirR4Async(
            new ConvertCdaToFhirR4Request
            {
                Content = LiveTestData.Cda,
                IncludeStandardizedCda = true,
            }
        );
        Assert.Contains(
            result.Entry,
            entry =>
                entry.Resource?.ResourceType == Hl7.Fhir.Model.ResourceType.DocumentReference
                && entry.Resource is Hl7.Fhir.Model.R4.DocumentReference doc
                && doc.Type?.Coding?.Any(coding => coding.Code == "StandardizedCda") == true
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToFhirR4WithPatientShouldConvert()
    {
        var result = await _api.Convert.CdaToFhirR4Async(
            new ConvertCdaToFhirR4Request { Content = LiveTestData.Cda, PatientId = "1234" }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.Equal("1234", patient.Id);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToFhirR4WithPatientIdentifierAndSystemShouldConvert()
    {
        var result = await _api.Convert.CdaToFhirR4Async(
            new ConvertCdaToFhirR4Request
            {
                Content = LiveTestData.Cda,
                PatientIdentifier = "1234",
                PatientIdentifierSystem = "GoodHealthClinic",
            }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.True(
            patient.Identifier?.Count > 0
                && patient.Identifier[0].Use == "usual"
                && patient
                    .Identifier[0]
                    .System?.Contains("GoodHealthClinic", StringComparison.Ordinal) == true
                && patient.Identifier[0].Value == "1234"
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToPdfShouldConvert()
    {
        var result = await _api.Convert.CdaToPdfAsync(
            new ConvertCdaToPdfRequest { Content = LiveTestData.Cda }
        );
        Assert.Equal(PdfMagicNumber, result.Take(4).ToArray());
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToCdaShouldConvert()
    {
        var result = await _api.Convert.FhirR4ToCdaAsync(
            new ConvertFhirR4ToCdaRequest { Content = LiveTestData.R4Bundle }
        );
        Assert.StartsWith("<?xml", result, StringComparison.Ordinal);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToOmopShouldConvert()
    {
        var result = await _api.Convert.FhirR4ToOmopAsync(
            new ConvertFhirR4ToOmopRequest { Content = LiveTestData.R4Bundle }
        );
        Assert.Equal(PkZipMagicNumber, result.Take(4).ToArray());
        using var archive = new ZipArchive(new MemoryStream(result), ZipArchiveMode.Read);
        Assert.NotEmpty(archive.Entries);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task InsightRiskProfileShouldReturnBundle()
    {
        var result = await _api.Insight.RiskProfileAsync(
            new InsightRiskProfileRequest
            {
                Content = LiveTestData.RiskProfileBundle,
                HccVersion = "22",
                PeriodEndDate = "2020-12-31",
                RaSegment = "community nondual aged",
            }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCombinedFhirR4BundlesShouldCombine()
    {
        var result = await _api.Convert.CombineFhirR4BundlesAsync(
            ConvertRequestFactory.GenerateConvertCombinedFhirBundlesRequestFromBundles([
                LiveTestData.R4Bundle,
                LiveTestData.R4Bundle,
            ])
        );
        Assert.Equal(2, result.Entry.Count);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCombinedFhirR4BundlesWithPatientShouldCombine()
    {
        var result = await _api.Convert.CombineFhirR4BundlesAsync(
            ConvertRequestFactory.GenerateConvertCombinedFhirBundlesRequestFromBundles(
                [LiveTestData.R4Bundle, LiveTestData.R4Bundle],
                "1234"
            )
        );
        Assert.Equal(2, result.Entry.Count);
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.Equal("1234", patient.Id);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCombinedFhirR4BundlesWithPatientIdentifierAndSystemShouldConvert()
    {
        var request = ConvertRequestFactory.GenerateConvertCombinedFhirBundlesRequestFromBundles([
            LiveTestData.R4Bundle,
            LiveTestData.R4Bundle,
        ]);
        request.PatientIdentifier = "1234";
        request.PatientIdentifierSystem = "GoodHealthClinic";

        var result = await _api.Convert.CombineFhirR4BundlesAsync(request);
        Assert.Equal(2, result.Entry.Count);
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.True(
            patient.Identifier?.Count > 0
                && patient.Identifier[0].Use == "usual"
                && patient
                    .Identifier[0]
                    .System?.Contains("GoodHealthClinic", StringComparison.Ordinal) == true
                && patient.Identifier[0].Value == "1234"
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertX12ToFhirR4ShouldReturnBundle()
    {
        var result = await _api.Convert.X12ToFhirR4Async(
            new ConvertX12ToFhirR4Request { Content = LiveTestData.X12Document }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertX12ToFhirR4WithPatientShouldReturnBundle()
    {
        var result = await _api.Convert.X12ToFhirR4Async(
            new ConvertX12ToFhirR4Request
            {
                Content = LiveTestData.X12Document,
                PatientId = "12/34",
            }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.Equal("12/34", patient.Id);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertX12ToFhirR4WithPatientIdentifierAndSystemShouldConvert()
    {
        var result = await _api.Convert.X12ToFhirR4Async(
            new ConvertX12ToFhirR4Request
            {
                Content = LiveTestData.X12Document,
                PatientIdentifier = "1234",
                PatientIdentifierSystem = "GoodHealthClinic",
            }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.True(
            patient.Identifier?.Count > 0
                && patient.Identifier[0].Use == "usual"
                && patient
                    .Identifier[0]
                    .System?.Contains("GoodHealthClinic", StringComparison.Ordinal) == true
                && patient.Identifier[0].Value == "1234"
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4CodeSystemShouldReturnCodeSystem()
    {
        var result = await _api.Terminology.GetFhirR4CodeSystemAsync(
            new GetFhirR4CodeSystemRequest { CodeSystem = "SNOMED" }
        );
        Assert.NotEmpty(result.Concept);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4CodeSystemWithPageShouldReturnCodeSystem()
    {
        var result = await _api.Terminology.GetFhirR4CodeSystemAsync(
            new GetFhirR4CodeSystemRequest
            {
                CodeSystem = "SNOMED",
                PageNumber = 0,
                PageSize = 2,
            }
        );
        Assert.NotEmpty(result.Concept);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4CodeSystemWithSearchShouldReturnCodeSystem()
    {
        var result = await _api.Terminology.GetFhirR4CodeSystemAsync(
            new GetFhirR4CodeSystemRequest
            {
                CodeSystem = "ICD-10-CM",
                ConceptContains = "myocardial infarction",
                PageNumber = 0,
                PageSize = 2,
            }
        );
        Assert.NotEmpty(result.Concept);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task SummarizeFhirR4CodeSystemsShouldReturnBundle()
    {
        var result = await _api.Terminology.SummarizeFhirR4CodeSystemsAsync();
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ConceptMapsShouldReturnBundle()
    {
        var result = await _api.Terminology.GetFhirR4ConceptMapsAsync();
        Assert.NotEmpty(result.Entry);
        Assert.All(
            result.Entry,
            entry =>
                Assert.Equal(Hl7.Fhir.Model.ResourceType.ConceptMap, entry.Resource?.ResourceType)
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task TranslateFhirR4ConceptMapWithCodeShouldTranslate()
    {
        var result = await _api.Terminology.TranslateFhirR4ConceptMapAsync(
            new TranslateFhirR4ConceptMapRequest { Code = "119981000146107" }
        );
        Assert.NotEmpty(result.Parameter);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task TranslateFhirR4ConceptMapWithCodeAndDomainShouldTranslate()
    {
        var result = await _api.Terminology.TranslateFhirR4ConceptMapAsync(
            new TranslateFhirR4ConceptMapRequest { Code = "119981000146107", Domain = "Condition" }
        );
        Assert.NotEmpty(result.Parameter);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task SummarizeFhirR4ValueSetScopeShouldReturnBundle()
    {
        var result = await _api.Terminology.SummarizeFhirR4ValueSetScopeAsync(
            new SummarizeFhirR4ValueSetScopeRequest { Scope = "http://loinc.org" }
        );
        Assert.NotEmpty(result.Entry);
        Assert.True(result.Entry.Count <= 10000);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetShouldReturnValueSet()
    {
        var result = await _api.Terminology.GetFhirR4ValueSetAsync(
            new GetFhirR4ValueSetRequest
            {
                Id = "00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2",
            }
        );
        Assert.NotNull(result.Compose?.Include);
        Assert.NotEmpty(result.Compose.Include);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task SummarizeFhirR4ValueSetShouldReturnValueSet()
    {
        var result = await _api.Terminology.SummarizeFhirR4ValueSetAsync(
            new SummarizeFhirR4ValueSetRequest
            {
                Id = "00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2",
            }
        );
        Assert.Equal(Hl7.Fhir.Model.ResourceType.ValueSet, result.ResourceType);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetScopesShouldReturnValueSet()
    {
        var result = await _api.Terminology.GetFhirR4ValueSetScopesAsync();
        Assert.NotNull(result.Compose?.Include);
        Assert.NotEmpty(result.Compose.Include);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetsByScopeWithoutPaginationShouldRaise()
    {
        await Assert.ThrowsAsync<OrchestrateClientException>(() =>
            _api.Terminology.GetFhirR4ValueSetsByScopeAsync(
                new GetFhirR4ValueSetsByScopeRequest { Scope = "http://loinc.org" }
            )
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetsByScopeWithPageAndScopeShouldReturnBundle()
    {
        var result = await _api.Terminology.GetFhirR4ValueSetsByScopeAsync(
            new GetFhirR4ValueSetsByScopeRequest
            {
                Scope = "http://loinc.org",
                PageNumber = 0,
                PageSize = 2,
            }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetsByScopeWithPageAndNameShouldReturnBundle()
    {
        var result = await _api.Terminology.GetFhirR4ValueSetsByScopeAsync(
            new GetFhirR4ValueSetsByScopeRequest
            {
                Name = "LP7839-6",
                PageNumber = 0,
                PageSize = 2,
            }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetsByScopeWithPageNameAndScopeShouldReturnBundle()
    {
        var result = await _api.Terminology.GetFhirR4ValueSetsByScopeAsync(
            new GetFhirR4ValueSetsByScopeRequest
            {
                Name = "LP7839-6",
                Scope = "http://loinc.org",
                PageNumber = 0,
                PageSize = 2,
            }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetFhirR4ValueSetsByScopeWithJustPageShouldReturnBundle()
    {
        var result = await _api.Terminology.GetFhirR4ValueSetsByScopeAsync(
            new GetFhirR4ValueSetsByScopeRequest { PageNumber = 0, PageSize = 2 }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task SummarizeFhirR4CodeSystemShouldReturnCodeSystem()
    {
        var result = await _api.Terminology.SummarizeFhirR4CodeSystemAsync(
            new SummarizeFhirR4CodeSystemRequest { CodeSystem = "SNOMED" }
        );
        Assert.True(result.Count > 0);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task GetAllFhirR4ValueSetsForCodesShouldReturnParameters()
    {
        var parameters = new Parameters
        {
            Parameter =
            [
                new Parameters.ParameterComponent
                {
                    Name = "code",
                    Value = new Hl7.Fhir.Model.FhirString("119981000146107"),
                },
                new Parameters.ParameterComponent
                {
                    Name = "system",
                    Value = new Hl7.Fhir.Model.FhirString("http://snomed.info/sct"),
                },
            ],
        };

        var result = await _api.Terminology.GetAllFhirR4ValueSetsForCodesAsync(parameters);
        Assert.NotEmpty(result.Parameter);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirDstu2ToFhirR4ShouldConvert()
    {
        var result = await _api.Convert.FhirDstu2ToFhirR4Async(
            new ConvertFhirDstu2ToFhirR4Request { Content = LiveTestData.Dstu2Bundle }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.Contains(
            patient.Identifier,
            identifier => identifier.ElementId == "id3" && identifier.Value == "12345A"
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirStu3ToFhirR4ShouldConvert()
    {
        var result = await _api.Convert.FhirStu3ToFhirR4Async(
            new ConvertFhirStu3ToFhirR4Request { Content = LiveTestData.Stu3Bundle }
        );
        var patient = GetEntryResourceByType<Hl7.Fhir.Model.R4.Patient>(
            result,
            Hl7.Fhir.Model.ResourceType.Patient
        );
        Assert.Contains(
            patient.Identifier,
            identifier => identifier.ElementId == "id3" && identifier.Value == "1234A"
        );
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToHealthLakeShouldConvert()
    {
        var result = await _api.Convert.FhirR4ToHealthLakeAsync(
            new ConvertFhirR4ToHealthLakeRequest { Content = LiveTestData.R4Bundle }
        );
        Assert.Equal(Hl7.Fhir.Model.BundleType.Collection, result.Type);
        Assert.Equal(Hl7.Fhir.Model.ResourceType.Bundle, result.Entry[0].Resource?.ResourceType);
        Assert.Equal(Hl7.Fhir.Model.BundleType.Batch, ((Bundle)result.Entry[0].Resource!).Type);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToHtmlShouldConvert()
    {
        var result = await _api.Convert.CdaToHtmlAsync(
            new ConvertCdaToHtmlRequest { Content = LiveTestData.Cda }
        );
        Assert.StartsWith("<html", result, StringComparison.Ordinal);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertCdaToFhirR4AlternativeEncodingShouldSendBytes()
    {
        var result = await _api.Convert.CdaToFhirR4Async(
            new ConvertCdaToFhirR4Request { Content = LiveTestData.EncodingCda }
        );
        Assert.NotEmpty(result.Entry);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToNemsisV34ShouldConvert()
    {
        var result = await _api.Convert.FhirR4ToNemsisV34Async(
            new ConvertFhirR4ToNemsisV34Request { Content = LiveTestData.NemsisBundle }
        );
        Assert.Contains("<EMSDataSet", result, StringComparison.Ordinal);
        Assert.DoesNotContain("<eOutcome.18", result, StringComparison.Ordinal);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToNemsisV35ShouldConvert()
    {
        var result = await _api.Convert.FhirR4ToNemsisV35Async(
            new ConvertFhirR4ToNemsisV35Request { Content = LiveTestData.NemsisBundle }
        );
        Assert.Contains("<EMSDataSet", result, StringComparison.Ordinal);
        Assert.Contains("<eOutcome.18", result, StringComparison.Ordinal);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToManifestShouldHaveCsvs()
    {
        var result = await _api.Convert.FhirR4ToManifestAsync(
            new ConvertFhirR4ToManifestRequest { Content = LiveTestData.R4Bundle }
        );
        Assert.Equal(PkZipMagicNumber, result.Take(4).ToArray());

        using var archive = new ZipArchive(new MemoryStream(result), ZipArchiveMode.Read);
        var names = archive.Entries.Select(entry => entry.FullName).ToList();
        Assert.Contains("patients.csv", names);
        Assert.Contains("encounters.csv", names);
        Assert.Contains("procedures.csv", names);
        Assert.Contains("conditions.csv", names);
        Assert.All(
            archive.Entries,
            entry =>
            {
                Assert.EndsWith(".csv", entry.FullName, StringComparison.Ordinal);
                Assert.True(entry.Length > 0);
            }
        );

        using var reader = new StreamReader(archive.GetEntry("patients.csv")!.Open());
        var content = await reader.ReadToEndAsync();
        Assert.Contains(",", content, StringComparison.Ordinal);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task ConvertFhirR4ToManifestWithDelimiterShouldHaveCsvsAndExpectedDelimiter()
    {
        var result = await _api.Convert.FhirR4ToManifestAsync(
            new ConvertFhirR4ToManifestRequest { Content = LiveTestData.R4Bundle, Delimiter = "|" }
        );

        using var archive = new ZipArchive(new MemoryStream(result), ZipArchiveMode.Read);
        using var reader = new StreamReader(archive.GetEntry("patients.csv")!.Open());
        var content = await reader.ReadToEndAsync();
        Assert.Contains("|", content, StringComparison.Ordinal);
    }

    [LiveFact(LiveTestEnvironment.OrchestrateApiKey)]
    public async Task WithTimeoutShouldTimeout()
    {
        using var httpClient = new HttpClient();
        var timeoutApi = new OrchestrateApi(
            httpClient,
            new OrchestrateClientOptions { TimeoutMs = 1 }
        );
        await Assert.ThrowsAnyAsync<Exception>(() =>
            timeoutApi.Convert.Hl7ToFhirR4Async(
                new ConvertHl7ToFhirR4Request { Content = LiveTestData.Hl7 }
            )
        );
    }

    private static int CountResources(Bundle bundle, Hl7.Fhir.Model.ResourceType resourceType) =>
        bundle.Entry.Count(entry => entry.Resource?.ResourceType == resourceType);

    private static TResource GetEntryResourceByType<TResource>(
        Bundle bundle,
        Hl7.Fhir.Model.ResourceType resourceType
    )
        where TResource : Hl7.Fhir.Model.Resource
    {
        return bundle.Entry.First(entry => entry.Resource?.ResourceType == resourceType).Resource
                as TResource
            ?? throw new InvalidOperationException($"Expected resource type '{resourceType}'.");
    }

    public void Dispose()
    {
        _httpClient.Dispose();
    }
}
