import { OrchestrateApi } from '../src/api';
import { hl7, cda, fhir, riskProfileBundle, x12Document, stu3FhirBundle, dstu2FhirBundle, nemsisBundle } from './data';
import dotenv from 'dotenv';
import { Binary, Bundle, BundleEntry, Encounter, Observation, Patient } from 'fhir/r4';
import {
  ClassifyConditionRequest,
  ClassifyMedicationRequest,
  ClassifyObservationRequest,
  StandardizeRequest,
} from "../src/terminology";
import { describe, it, expect, test } from "vitest";

dotenv.config({ path: "../.env" });
const orchestrate = new OrchestrateApi();
const pkZipMagicNumber = new Int8Array([80, 75, 3, 4]);

describe("classify condition", () => {
  const requests: ClassifyConditionRequest[] = [
    {
      code: "119981000146107",
      system: "http://snomed.info/sct",
    },
    {
      code: "119981000146107",
      system: "SNOMED",
    },
  ];
  const cases = requests.map((input) => ({ input }));
  test.each(cases)("should classify single $input", async ({ input }: { input: ClassifyConditionRequest; }) => {
    const result = await orchestrate.terminology.classifyCondition(input);
    expect(result).toBeDefined();
    expect(result.cciAcute).toBeTruthy();
  });

  it("should classify batch", async () => {
    const results = await orchestrate.terminology.classifyCondition(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    results.forEach((result) => {
      expect(result.cciAcute).toBeTruthy();
    });
  });
});

describe("classify medication", () => {
  const requests: ClassifyMedicationRequest[] = [
    {
      code: "2468231",
      system: "http://www.nlm.nih.gov/research/umls/rxnorm",
    },
    {
      code: "2468231",
      system: "RxNorm",
    },
  ];
  const cases = requests.map((input) => ({ input }));
  test.each(cases)("should classify single $input", async ({ input }: { input: ClassifyMedicationRequest; }) => {
    const result = await orchestrate.terminology.classifyMedication(input);
    expect(result).toBeDefined();
    expect(result.rxNormGeneric).toBeTruthy();
  });

  it("should classify batch", async () => {
    const results = await orchestrate.terminology.classifyMedication(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    results.forEach((result) => {
      expect(result.rxNormGeneric).toBeTruthy();
    });
  });
});

describe("classify observation", () => {
  const requests: ClassifyObservationRequest[] = [
    {
      code: "94558-4",
      system: "http://loinc.org",
    },
    {
      code: "94558-4",
      system: "LOINC",
    },
  ];
  const cases = requests.map((input) => ({ input }));
  test.each(cases)("should classify single $input", async ({ input }: { input: ClassifyObservationRequest; }) => {
    const result = await orchestrate.terminology.classifyObservation(input);
    expect(result).toBeDefined();
    expect(result.loincClass).toBe("MICRO");
  });

  it("should classify with name", async () => {
    const results = await orchestrate.terminology.classifyObservation(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    results.forEach((result) => {
      expect(result.loincClass).toBe("MICRO");
    });
  });
});

describe("standardize condition", () => {
  const requests: StandardizeRequest[] = [
    {
      code: "370221004",
    },
    {
      code: "J45.50",
    },
    {
      display: "dm2",
    },
  ];
  const expected = ["370221004", "J45.50", "44054006"];
  const cases = requests.map((input, index) => ({ input, expected: expected[index] }));
  test.each(cases)(
    "should standardize single $input",
    async ({ input, expected }: { input: StandardizeRequest; expected: string; }) => {
      const result = await orchestrate.terminology.standardizeCondition(input);
      expect(result).toBeDefined();
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected);
    },
  );

  it("should standardize batch", async () => {
    const results = await orchestrate.terminology.standardizeCondition(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(3);
    results.forEach((result, index) => {
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected[index]);
    });
  });
});

describe("standardize lab", () => {
  const requests: StandardizeRequest[] = [
    {
      code: "4548-4",
    },
    {
      display: "hba1c 1/15/22 from outside lab",
    },
  ];
  const expected = ["4548-4", "43396009"];
  const cases = requests.map((input, index) => ({ input, expected: expected[index] }));
  test.each(cases)(
    "should standardize single $input",
    async ({ input, expected }: { input: StandardizeRequest; expected: string; }) => {
      const result = await orchestrate.terminology.standardizeLab(input);
      expect(result).toBeDefined();
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding.map((c) => c.code)).toContain(expected);
    },
  );

  it("should standardize batch", async () => {
    const results = await orchestrate.terminology.standardizeLab(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    console.log(JSON.stringify(results));
    results.forEach((result, index) => {
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding.map((c) => c.code)).toContain(expected[index]);
    });
  });
});

describe("standardize medication", () => {
  const requests: StandardizeRequest[] = [
    {
      code: "861004",
      system: "RxNorm",
    },
    {
      code: "59267-1000-02",
    },
    {
      display: "Jentadueto extended (linagliptin 2.5 / metFORMIN  1000mg)",
    },
  ];
  const expected = ["861004", "59267100002", "1796093"];
  const cases = requests.map((input, index) => ({ input, expected: expected[index] }));

  test.each(cases)(
    "should standardize single $input",
    async ({ input, expected }: { input: StandardizeRequest; expected: string; }) => {
      const result = await orchestrate.terminology.standardizeMedication(input);
      expect(result).toBeDefined();
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected);
    },
  );

  it("should standardize batch", async () => {
    const results = await orchestrate.terminology.standardizeMedication(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(3);
    results.forEach((result, index) => {
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected[index]);
    });
  });
});

describe("standardize observation", () => {
  const requests: StandardizeRequest[] = [
    {
      code: "8480-6",
    },
    {
      display: "BMI",
    },
  ];
  const expected = ["8480-6", "39156-5"];
  const cases = requests.map((input, index) => ({ input, expected: expected[index] }));

  test.each(cases)(
    "should standardize single $input",
    async ({ input, expected }: { input: StandardizeRequest; expected: string; }) => {
      const result = await orchestrate.terminology.standardizeObservation(input);
      expect(result).toBeDefined();
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected);
    },
  );

  it("should standardize batch", async () => {
    const results = await orchestrate.terminology.standardizeObservation(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    results.forEach((result, index) => {
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected[index]);
    });
  });
});

describe("standardize procedure", () => {
  const requests: StandardizeRequest[] = [
    {
      code: "80146002",
    },
    {
      display: "ct head&neck",
    },
  ];
  const expected = ["80146002", "429858000"];
  const cases = requests.map((input, index) => ({ input, expected: expected[index] }));

  test.each(cases)(
    "should standardize single $input",
    async ({ input, expected }: { input: StandardizeRequest; expected: string; }) => {
      const result = await orchestrate.terminology.standardizeProcedure(input);
      expect(result).toBeDefined();
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected);
    },
  );

  it("should standardize batch", async () => {
    const results = await orchestrate.terminology.standardizeProcedure(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    results.forEach((result, index) => {
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected[index]);
    });
  });
});

describe("standardize radiology", () => {
  const requests: StandardizeRequest[] = [
    {
      code: "711232001",
      system: "SNOMED",
    },
    {
      display: "CT scan of head w/o iv contrast 3d ago@StJoes",
    },
  ];
  const expected = ["711232001", "30799-1"];
  const cases = requests.map((input, index) => ({ input, expected: expected[index] }));

  test.each(cases)(
    "should standardize single $input",
    async ({ input, expected }: { input: StandardizeRequest; expected: string; }) => {
      const result = await orchestrate.terminology.standardizeRadiology(input);
      expect(result).toBeDefined();
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected);
    },
  );

  it("should standardize batch", async () => {
    const results = await orchestrate.terminology.standardizeRadiology(requests);
    expect(results).toBeDefined();
    expect(results.length).toBe(2);
    results.forEach((result, index) => {
      expect(result.coding.length).toBeGreaterThan(0);
      expect(result.coding[0].code).toBe(expected[index]);
    });
  });
});

describe("convert hl7 to fhir r4", () => {
  it("should convert hl7", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: hl7,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should convert hl7 with patient", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: hl7,
      patientID: "12/34",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("12/34");
  });

  it("should convert hl7 with patientIdentifierAndSystem", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: hl7,
      patientIdentifier: "1234",
      patientIdentifierSystem: "GoodHealthClinic",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");

    expect(patientResource).toBeDefined();
    const patient = patientResource?.resource as Patient;
    expect(patient).toBeDefined();

    expect(
      patient.identifier?.[0]?.use === "usual" &&
      patient.identifier?.[0]?.system?.includes("GoodHealthClinic") &&
      patient.identifier?.[0]?.value === "1234"
    ).toBe(true);
  });

  it("should convert hl7 with timezone", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: hl7,
      tz: "America/New_York",
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const encounter = result.entry?.find((entry) => entry.resource?.resourceType === "Encounter")?.resource as Encounter;
    expect(encounter).toBeDefined();
    expect(encounter?.period?.start).toBe("2014-11-07T14:40:00-05:00");
  });

  it("should use UTC when no timezone is supplied", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: hl7,
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const encounter = result.entry?.find((entry) => entry.resource?.resourceType === "Encounter")?.resource as Encounter;
    expect(encounter).toBeDefined();
    expect(encounter?.period?.start).toBe("2014-11-07T14:40:00+00:00");
  });

  const labHl7 = (`
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
`)
  const transcriptionHl7 = (`
MSH|^~\&||TX|||20110706100000||ORU^R01|||2.3
PID|1||123456||LastName^FirstName||20000101|M||||||||||7890
PV1|1|I||||||||||||||||||||||||||||||||||||||||||20110706100000
ORC|RE|^SCM|||||||20110706100000|||010400^DOE MD^JOHN^^^^
OBR|1|^SCM|001XYZ555^SCM|CH9^CHEST SPECIAL VIEWS|||20110706100000|||||||20110706100000||010400^DOE MD^JOHN^^^^|||||||||P||^^^20110706100000^^R|~~~~||||010400^DOE MD^JOHN|~|^UNKNOWN^TECHNOLOGIST^^^^|010400^DOE MD^JOHN^^^^
OBX|1|ST|&GDT^^GDT||Line 1||||||F
OBX|2|ST|&GDT^Label^GDT||Line 2||||||F
OBX|3|ST|&GDT^&Not a Label^GDT||Line 3||||||F
OBX|4|ST|Dictation TS|2|Dictated by: Tue Mar 18, 2025  1:06:45 PM EDT [INTERFACE, INCOMING RADIANT IMAGE AVAILABILITY]||||||Final|||||E175762^MILLER^AMANDA^^^^^^PROVID^^^^PROVID^^^^^^^^RT|||||||||
`)
  it("should convert lab hl7 with hint", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: labHl7, processingHint: "lab",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const observations = result.entry?.filter(
      (entry) => entry.resource?.resourceType === "Observation"
    ) as BundleEntry<Observation>[];
    expect(observations.length).toBe(9);
  });

  it("should convert lab hl7 without hint", async () => {
    const unhintedResult = await orchestrate.convert.hl7ToFhirR4({
      content: labHl7,
    });
    const defaultResult = await orchestrate.convert.hl7ToFhirR4({
      content: labHl7, processingHint: "default",
    });
    for (const result of [unhintedResult, defaultResult]) {
      expect(result).toBeDefined();
      expect(result.resourceType).toBe("Bundle");
      expect(result.entry?.length).toBeGreaterThan(0);
      const observations = result.entry?.filter(
        (entry) => entry.resource?.resourceType === "Observation"
      ) as BundleEntry<Observation>[];
      expect(observations.length).toBe(0);
    }
  });

  it("should convert transcription hl7", async () => {
    const result = await orchestrate.convert.hl7ToFhirR4({
      content: transcriptionHl7, processingHint: "transcription",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const binaries = result.entry?.filter(
      (entry) => entry.resource?.resourceType === "Binary"
    ) as BundleEntry<Binary>[];
    expect(binaries.length).toBe(1);
  });

  it("should convert transcription hl7 without hint", async () => {
    const unhintedResult = await orchestrate.convert.hl7ToFhirR4({
      content: transcriptionHl7,
    });
    const defaultResult = await orchestrate.convert.hl7ToFhirR4({
      content: transcriptionHl7, processingHint: "default",
    });
    for (const result of [unhintedResult, defaultResult]) {
      expect(result).toBeDefined();
      expect(result.resourceType).toBe("Bundle");
      expect(result.entry?.length).toBeGreaterThan(0);
      const binaries = result.entry?.filter(
        (entry) => entry.resource?.resourceType === "Binary"
      ) as BundleEntry<Binary>[];
      expect(binaries.length).toBe(0);
    }
  });
});

describe("convert cda to fhir r4", () => {
  it("should convert cda", async () => {
    const result = await orchestrate.convert.cdaToFhirR4({
      content: cda,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should convert cda with includeStandardizedCda", async () => {
    const result = await orchestrate.convert.cdaToFhirR4({
      content: cda,
      includeStandardizedCda: true,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const documentReferences = result.entry?.filter(
      (entry) => entry.resource?.resourceType === "DocumentReference"
    );
    const standardizedCdaDocumentReference = documentReferences?.find(
      (docRef) =>
        (docRef.resource)?.type?.coding?.some(
          (coding) => coding.code === "StandardizedCda"
        )
    );
    expect(standardizedCdaDocumentReference).toBeDefined();
  });

  it("should convert cda with includeOriginalCda", async () => {
    const result = await orchestrate.convert.cdaToFhirR4({
      content: cda,
      includeOriginalCda: true,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const documentReferences = result.entry?.filter(
      (entry) => entry.resource?.resourceType === "DocumentReference"
    );
    const standardizedCdaDocumentReference = documentReferences?.find(
      (docRef) =>
        (docRef.resource)?.type?.coding?.some(
          (coding) => coding.code === "Cda"
        )
    );
    expect(standardizedCdaDocumentReference).toBeDefined();
  });

  it("should convert cda with patient", async () => {
    const result = await orchestrate.convert.cdaToFhirR4({
      content: cda,
      patientID: "1234",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});

it("should convert cda with patientIdentifierAndSystem", async () => {
  const result = await orchestrate.convert.cdaToFhirR4({
    content: cda,
    patientIdentifier: "1234",
    patientIdentifierSystem: "GoodHealthClinic",
  });
  expect(result).toBeDefined();
  expect(result.resourceType).toBe("Bundle");
  expect(result.entry?.length).toBeGreaterThan(0);
  const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");

  expect(patientResource).toBeDefined();
  const patient = patientResource?.resource as Patient;
  expect(patient).toBeDefined();

  expect(
    patient.identifier?.[0]?.use === "usual" &&
    patient.identifier?.[0]?.system?.includes("GoodHealthClinic") &&
    patient.identifier?.[0]?.value === "1234"
  ).toBe(true);
});

describe("convert cda to pdf", () => {
  it("should convert cda", async () => {
    const result = await orchestrate.convert.cdaToPdf({
      content: cda,
    });
    expect(result).toBeDefined();
    const resultIntegers = new Int8Array(result);
    const pdfMagicNumber = new Int8Array([37, 80, 68, 70]);
    expect(resultIntegers.slice(0, 4)).toStrictEqual(pdfMagicNumber);
  });
});

describe("convert fhir r4 to cda", () => {
  it("should convert fhir", async () => {
    const result = await orchestrate.convert.fhirR4ToCda({
      content: fhir,
    });
    expect(result).toBeDefined();
    expect(result).toContain("<?xml");
  });
});

describe("convert fhir r4 to omop", () => {
  it("should convert fhir", async () => {
    const result = await orchestrate.convert.fhirR4ToOmop({
      content: fhir,
    });
    expect(result).toBeDefined();
    const resultIntegers = new Int8Array(result);
    expect(resultIntegers.slice(0, 4)).toStrictEqual(pkZipMagicNumber);
  });
});

describe("convert x12 to fhir r4", () => {
  it("should convert x12", async () => {
    const result = await orchestrate.convert.x12ToFhirR4({
      content: x12Document,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should convert x12 with patient", async () => {
    const result = await orchestrate.convert.x12ToFhirR4({
      content: x12Document,
      patientID: "1234",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});

it("should convert x12 with patientIdentifierAndSystem", async () => {
  const result = await orchestrate.convert.x12ToFhirR4({
    content: x12Document,
    patientIdentifier: "1234",
    patientIdentifierSystem: "GoodHealthClinic",
  });
  expect(result).toBeDefined();
  expect(result.resourceType).toBe("Bundle");
  expect(result.entry?.length).toBeGreaterThan(0);
  const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");

  expect(patientResource).toBeDefined();
  const patient = patientResource?.resource as Patient;
  expect(patient).toBeDefined();

  expect(
    patient.identifier?.[0]?.use === "usual" &&
    patient.identifier?.[0]?.system?.includes("GoodHealthClinic") &&
    patient.identifier?.[0]?.value === "1234"
  ).toBe(true);
});


describe("insight risk profile", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.insight.riskProfile({
      hccVersion: "22",
      periodEndDate: "2020-12-31",
      raSegment: "community nondual aged",
      content: riskProfileBundle,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });
});

describe("get fhir r4 code system", () => {
  it("should return a code_system", async () => {
    const result = await orchestrate.terminology.getFhirR4CodeSystem({
      codeSystem: "SNOMED",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.concept?.length).toBeGreaterThan(0);
  }, 10000);

  it("should return a code system with page", async () => {
    const result = await orchestrate.terminology.getFhirR4CodeSystem({
      codeSystem: "SNOMED",
      pageNumber: 1,
      pageSize: 2,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.concept?.length).toBe(2);
  });

  it("should return a code system with search", async () => {
    const result = await orchestrate.terminology.getFhirR4CodeSystem({
      codeSystem: "ICD-10-CM",
      conceptContains: "myocardial infarction",
      pageNumber: 0,
      pageSize: 2,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.concept?.length).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 code systems", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.terminology.summarizeFhirR4CodeSystems();
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });
});

describe("get fhir r4 concept maps", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.terminology.getFhirR4ConceptMaps();
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    result.entry?.forEach((entry) => {
      expect(entry.resource?.resourceType).toBe("ConceptMap");
    });
  });
});

describe("translate fhir r4 concept map", () => {
  it("should translate code", async () => {
    const result = await orchestrate.terminology.translateFhirR4ConceptMap({
      code: "119981000146107",
    });
    expect(result).toBeDefined();
    expect(result.parameter?.length).toBeGreaterThan(0);
  });

  it("should translate code and system", async () => {
    const result = await orchestrate.terminology.translateFhirR4ConceptMap({
      code: "119981000146107",
      domain: "Condition",
    });
    expect(result).toBeDefined();
    expect(result.parameter?.length).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 value set scope", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.terminology.summarizeFhirR4ValueSetScope({
      scope: "http://loinc.org",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    expect(result.entry?.length).toBeLessThanOrEqual(10000);
  }, 10000);
});

describe("get fhir r4 value set", () => {
  it("should return a value set", async () => {
    const result = await orchestrate.terminology.getFhirR4ValueSet({
      id: "00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("ValueSet");
    expect(result.compose?.include?.length).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 value set", () => {
  it("should return a value set", async () => {
    const result = await orchestrate.terminology.summarizeFhirR4ValueSet({
      id: "00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("ValueSet");
  });
});

describe("get fhir r4 value set scopes", () => {
  it("should return a value set", async () => {
    const result = await orchestrate.terminology.getFhirR4ValueSetScopes();
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("ValueSet");
    expect(result.compose?.include.length).toBeGreaterThan(0);
  });
});

describe("get fhir r4 value set by scope", () => {
  it("should throw without pagination", async () => {
    await expect(
      orchestrate.terminology.getFhirR4ValueSetsByScope({
        scope: "http://loinc.org",
      }),
    ).rejects.toThrow();
  });

  it("should return a bundle with page and scope", async () => {
    const result = await orchestrate.terminology.getFhirR4ValueSetsByScope({
      scope: "http://loinc.org",
      pageNumber: 1,
      pageSize: 2,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });

  it("should return a bundle with page and name", async () => {
    const result = await orchestrate.terminology.getFhirR4ValueSetsByScope({
      name: "LP7839-6",
      pageNumber: 1,
      pageSize: 2,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });

  it("should return a bundle with page, name, and scope", async () => {
    const result = await orchestrate.terminology.getFhirR4ValueSetsByScope({
      name: "LP7839-6",
      scope: "http://loinc.org",
      pageNumber: 1,
      pageSize: 2,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });

  it("should return a bundle with just page", async () => {
    const result = await orchestrate.terminology.getFhirR4ValueSetsByScope({
      pageNumber: 1,
      pageSize: 2,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 code system", () => {
  it("should return a code system", async () => {
    const result = await orchestrate.terminology.summarizeFhirR4CodeSystem({
      codeSystem: "SNOMED",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.count).toBeGreaterThan(0);
  });
});

describe("get all fhir r4 value sets for codes", () => {
  it("should return parameters", async () => {
    const result = await orchestrate.terminology.getAllFhirR4ValueSetsForCodes({
      resourceType: "Parameters",
      parameter: [
        {
          name: "code",
          valueString: "119981000146107",
        },
        {
          name: "system",
          valueString: "http://snomed.info/sct",
        },
      ],
    });
    expect(result).toBeDefined();
    expect(result.parameter?.length).toBeGreaterThan(0);
  });
});

describe("convert combined fhir r4 bundles", () => {
  it("should combine", async () => {
    const bundles = `
${JSON.stringify(fhir)}
${JSON.stringify(fhir)}
`;

    const result = await orchestrate.convert.combineFhirR4Bundles({
      content: bundles,
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should combine with patient", async () => {
    const bundles = `
${JSON.stringify(fhir)}
${JSON.stringify(fhir)}
`;

    const result = await orchestrate.convert.combineFhirR4Bundles({
      content: bundles,
      patientID: "1234",
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});

it("should combine with patientIdentifierAndSystem", async () => {
  const bundles = `
${JSON.stringify(fhir)}
${JSON.stringify(fhir)}
`;

  const result = await orchestrate.convert.combineFhirR4Bundles({
    content: bundles,
    patientIdentifier: "1234",
    patientIdentifierSystem: "GoodHealthClinic",
  });
  expect(result).toBeDefined();
  expect(result.resourceType).toBe("Bundle");
  expect(result.entry?.length).toBeGreaterThan(0);
  const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");

  expect(patientResource).toBeDefined();
  const patient = patientResource?.resource as Patient;
  expect(patient).toBeDefined();

  expect(
    patient.identifier?.[0]?.use === "usual" &&
    patient.identifier?.[0]?.system?.includes("GoodHealthClinic") &&
    patient.identifier?.[0]?.value === "1234"
  ).toBe(true);
});

describe("convert fhir stu3 to fhir r4", () => {
  it("should convert", async () => {
    const result = await orchestrate.convert.fhirStu3ToFhirR4({
      content: stu3FhirBundle
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient")?.resource as Patient;
    expect(patientResource).toBeDefined();
    const expectedIdentifier = patientResource?.identifier?.find((identifier) => identifier.id === "id3");
    expect(expectedIdentifier).toBeDefined();
    expect(expectedIdentifier?.value).toBe("1234A");
  });
});

describe("convert fhir dstu2 to fhir r4", () => {
  it("should convert", async () => {
    const result = await orchestrate.convert.fhirDstu2ToFhirR4({
      content: dstu2FhirBundle
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient")?.resource as Patient;
    expect(patientResource).toBeDefined();
    const expectedIdentifier = patientResource?.identifier?.find((identifier) => identifier.id === "id3");
    expect(expectedIdentifier).toBeDefined();
    expect(expectedIdentifier?.value).toBe("12345A");
  });
});

describe("convert fhir r4 to health lake", () => {
  it("should convert", async () => {
    const result = await orchestrate.convert.fhirR4ToHealthLake({
      content: fhir
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    expect(result.type).toBe("collection");
    expect(result.entry?.[0].resource?.resourceType).toBe("Bundle");
    const batchBundle = result.entry?.[0].resource as Bundle;
    expect(batchBundle.type).toBe("batch");
  });
});

describe("convert cda to html", () => {
  it("should convert", async () => {
    const result = await orchestrate.convert.cdaToHtml({
      content: cda
    });

    expect(result).toBeDefined();
    expect(result).toContain("<html");
  });
});

describe("convert fhir r4 to nemsis v34", () => {
  it("should convert", async () => {
    const result = await orchestrate.convert.fhirR4ToNemsisV34({
      content: nemsisBundle
    });

    expect(result).toBeDefined();
    expect(result).toContain("<EMSDataSet");
    expect(result).not.toContain("<eOutcome.18");
  });
});

describe("convert fhir r4 to nemsis v35", () => {
  it("should convert", async () => {
    const result = await orchestrate.convert.fhirR4ToNemsisV35({
      content: nemsisBundle
    });

    expect(result).toBeDefined();
    expect(result).toContain("<EMSDataSet");
    expect(result).toContain("<eOutcome.18");
  });
});

describe("convert fhir r4 to manifest", async () => {
  it("should return a buffer", async () => {
    const result = await orchestrate.convert.fhirR4ToManifest({
      content: fhir,
    });

    expect(result).toBeDefined();
    console.log(typeof result);
    const resultIntegers = new Int8Array(result);
    expect(resultIntegers.slice(0, 4)).toStrictEqual(pkZipMagicNumber);
  });

  it("should return a buffer when delimiter specified ", async () => {
    const result = await orchestrate.convert.fhirR4ToManifest({
      content: fhir,
      delimiter: "|",
    });

    expect(result).toBeDefined();
    console.log(typeof result);
    const resultIntegers = new Int8Array(result);
    expect(resultIntegers.slice(0, 4)).toStrictEqual(pkZipMagicNumber);
  });
});