import { Bundle } from 'fhir/r4';
import { OrchestrateApi } from '../src/api';
import { config } from 'dotenv';
import { describe, expect, it } from '@jest/globals'

config({ path: '../.env' });
const apiKey = process.env.ROSETTA_API_KEY || "";
const rosettaUrl = process.env.ROSETTA_BASE_URL || undefined;
const additonalHeaders = process.env.ROSETTA_ADDITIONAL_HEADERS ? JSON.parse(process.env.ROSETTA_ADDITIONAL_HEADERS) : undefined;

const orchestrate = new OrchestrateApi({
  apiKey: apiKey,
  baseUrl: rosettaUrl,
  additionalHeaders: additonalHeaders,
});

const cda = (`
<?xml-stylesheet type="text/xsl" href=""?>
<ClinicalDocument xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 cda.xsd" moodCode="EVN" xmlns="urn:hl7-org:v3">
  <realmCode code="US" />
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040" />
  <templateId root="2.16.840.1.113883.10" extension="IMPL_CDAR2_LEVEL1" />
  <templateId root="2.16.840.1.113883.10.20.22.1.1" />
  <templateId root="2.16.840.1.113883.10.20.22.1.2" />
  <id root="3d1e9964-5fbd-4180-85af-0d473e3b43ec" />
  <code code="34133-9" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Summary of Episode Note" />
  <title>Medical Summary Document</title>
  <effectiveTime value="20150205121815-0500" />
  <confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25" codeSystemName="HL7 Confidentiality Code" displayName="Normal" />
  <languageCode code="en-US" />
  <recordTarget typeCode="RCT" contextControlCode="OP">
    <patientRole classCode="PAT">
      <id root="1.3.6.1.4.1.37608" extension="IheTestPatient" />
      <addr>
        <streetAddressLine>34 Drury Lane</streetAddressLine>
        <city>Disney Land</city>
        <state>CA</state>
        <postalCode>90210</postalCode>
      </addr>
      <telecom value="534-555-6666" use="HP" />
      <patient classCode="PSN" determinerCode="INSTANCE">
        <name>
          <given>Patient</given>
          <family>Smith</family>
        </name>
        <administrativeGenderCode code="F" codeSystem="DemoNamespace" codeSystemName="DemoNamespace" displayName="Female" />
        <birthTime value="19560813000000-0400" />
        <maritalStatusCode nullFlavor="UNK" />
        <raceCode nullFlavor="UNK" />
        <ethnicGroupCode nullFlavor="UNK" />
      </patient>
    </patientRole>
  </recordTarget>
  <component>
    <structuredBody>
      <component>
        <section classCode="DOCSECT" moodCode="EVN">
          <templateId root="2.16.840.1.113883.10.20.22.2.4.1" />
          <templateId root="2.16.840.1.113883.10.20.22.2.4" />
          <id root="175b3e57-db29-43e4-8158-e785594c9845" />
          <code code="8716-3" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Vital Signs" />
          <title>Vital Signs</title>
          <text mediaType="text/x-hl7-text+xml">No Vital Signs Available</text>
          <entry>
            <organizer classCode="CLUSTER" moodCode="EVN">
              <templateId root="2.16.840.1.113883.10.20.22.4.26" />
              <id nullFlavor="UNK" />
              <code code="46680005" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED CT" displayName="Vital signs" />
              <statusCode code="completed" />
              <effectiveTime nullFlavor="UNK" />
              <component>
                <observation classCode="OBS" moodCode="EVN" negationInd="true">
                  <templateId root="2.16.840.1.113883.10.20.22.4.27" />
                  <id nullFlavor="UNK" />
                  <code nullFlavor="UNK" />
                  <statusCode code="completed" />
                  <effectiveTime nullFlavor="UNK" />
                  <value xsi:type="PQ" nullFlavor="NI" />
                </observation>
              </component>
            </organizer>
          </entry>
        </section>
      </component>
    </structuredBody>
  </component>
</ClinicalDocument>
`);

const hl7 = (`
MSH|^~\\&|LAB|MYFAC|LAB||201411130917||ORU^R01|3216598|D|2.3|||AL|NE|
PID|1|ABC123DF|AND234DA_PID3|PID_4_ALTID|Smith^Patient^M||19670202 |F|||2222 22 st^^LAKE COUNTRY^NY^22222||222-222-2222|||||7890|
PV1|1|O|MYFACSOMPL||||^Smith^Patient^^^^^XAVS|||||||||||REF||SELF|||||||||||||||||||MYFAC||REG|||201411071440||||||||23390^PV1_52Smith^PV1_52Patient^H^^Dr^^PV1_52Mnemonic|
ORC|RE|PT103933301.0100|||CM|N|||201411130917|^John^Doctor^J.^^^^KYLA||^Smith^Patient^^^^^XAVS|MYFAC|
OBR|1|PT1311:H00001R301.0100|PT1311:H00001R|301.0100^Complete Blood Count (CBC)^00065227^57021-8^CBC \\T\\ Auto Differential^pCLOCD|R||201411130914|||KYLA||||201411130914||^Smith^Patient^^^^^XAVS||00065227||||201411130915||LAB|F||^^^^^R|^Smith^Patient^^^^^XAVS|
OBX|1|NM|301.0500^White Blood Count (WBC)^00065227^6690-2^Leukocytes^pCLOCD|1|10.1|10\\S\\9/L|3.1-9.7|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|2|NM|301.0600^Red Blood Count (RBC)^00065227^789-8^Erythrocytes^pCLOCD|1|3.2|10\\S\\12/L|3.7-5.0|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|3|NM|301.0700^Hemoglobin (HGB)^00065227^718-7^Hemoglobin^pCLOCD|1|140|g/L|118-151|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|4|NM|301.0900^Hematocrit (HCT)^00065227^4544-3^Hematocrit^pCLOCD|1|0.34|L/L|0.33-0.45|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|5|NM|301.1100^MCV^00065227^787-2^Mean Corpuscular Volume^pCLOCD|1|98.0|fL|84.0-98.0|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|6|NM|301.1300^MCH^00065227^785-6^Mean Corpuscular Hemoglobin^pCLOCD|1|27.0|pg|28.3-33.5|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|7|NM|301.1500^MCHC^00065227^786-4^Mean Corpuscular Hemoglobin Concentration^pCLOCD|1|330|g/L|329-352|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|8|NM|301.1700^RDW^00065227^788-0^Erythrocyte Distribution Width^pCLOCD|1|12.0|%|12.0-15.0|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|9|NM|301.1900^Platelets^00065227^777-3^Platelets^pCLOCD|1|125|10\\S\\9/L|147-375|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|10|NM|301.2100^Neutrophils^00065227^751-8^Neutrophils^pCLOCD|1|8.0|10\\S\\9/L|1.2-6.0|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|11|NM|301.2300^Lymphocytes^00065227^731-0^Lymphocytes^pCLOCD|1|1.0|10\\S\\9/L|0.6-3.1|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|12|NM|301.2500^Monocytes^00065227^742-7^Monocytes^pCLOCD|1|1.0|10\\S\\9/L|0.1-0.9|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|13|NM|301.2700^Eosinophils^00065227^711-2^Eosinophils^pCLOCD|1|0.0|10\\S\\9/L|0.0-0.5|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|14|NM|301.2900^Basophils^00065227^704-7^Basophils^pCLOCD|1|0.0|10\\S\\9/L|0.0-0.2|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
ZDR||^Smith^Patient^^^^^XAVS^^^^^XX^^ATP|
ZPR||
`);

const fhir = {
  "resourceType": "Bundle",
  "type": "batch-response",
  "entry": [
    {
      "fullUrl": "https://api.rosetta.careevolution.com/Patient/35b77437-425d-419c-90b5-af4bc433ebe9",
      "resource": {
        "resourceType": "Patient",
        "id": "35b77437-425d-419c-90b5-af4bc433ebe9",
        "meta": {
          "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
        },
        "identifier": [
          {
            "use": "usual",
            "type": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                  "code": "MR"
                }
              ]
            },
            "system": "urn:oid:1.3.6.1.4.1.37608",
            "value": "IheTestPatient"
          },
          {
            "system": "http://rosetta.careevolution.com/identifiers/Proprietary/1.3.6.1.4.1.37608",
            "value": "IheTestPatient"
          }
        ],
        "name": [
          {
            "use": "official",
            "family": "Smith",
            "given": [
              "Patient"
            ]
          }
        ],
        "telecom": [
          {
            "system": "phone",
            "value": "534-555-6666",
            "use": "home"
          }
        ],
        "gender": "female",
        "birthDate": "1956-08-13",
        "deceasedBoolean": false,
        "address": [
          {
            "use": "home",
            "line": [
              "34 Drury Lane"
            ],
            "city": "Disney Land",
            "state": "CA",
            "postalCode": "90210"
          }
        ]
      }
    }
  ]
} as Bundle;

const x12Document = (`ISA*00*          *00*          *ZZ*SUBMITTERID    *ZZ*RECEIVERID     *230616*1145*^*00501*000000001*0*T*:~
GS*HC*SENDERCODE*RECEIVERCODE*20230627*11301505*123456789*X*005010X222A1~
ST*837*0034*005010X223A1~
BHT*0019*00*3920394930203*20100816*1615*CH~
NM1*41*2*HOWDEE HOSPITAL*****46*0123456789~
PER*IC*BETTY RUBBLE*TE*9195551111~
NM1*40*2*BCBSNC*****46*987654321~
HL*1**20*1~
NM1*85*2*HOWDEE HOSPITAL*****XX*1245011012~
N3*123 HOWDEE BLVD~
N4*DURHAM*NC*27701~
REF*EI*123456789~
PER*IC*WILMA RUBBLE*TE*9195551111*FX*6145551212~
HL*2*1*22*0~
SBR*P*18*XYZ1234567******BL~
NM1*IL*1*DOUGH*MARY****MI*24672148306~
N3*BOX 12312~
N4*DURHAM*NC*27715~
DMG*D8*19670807*F~
NM1*PR*2*BCBSNC*****PI*987654321~
CLM*2235057*200***13:A:1***A**Y*Y~
DTP*434*RD8*20100730-20100730~
CL1*1*9*01~
REF*F8*ASD0000123~
HI*BK:25000~
HI*BF:78901~
HI*BR:4491:D8:20100730~
HI*BH:41:D8:20100501*BH:27:D8:20100715*BH:33:D8:20100415*BH:C2:D8:20100410~
HI*BE:30:::20~
HI*BG:01~
NM1*71*1*SMITH*ELIZABETH*AL***34*243898989~
REF*1G*P97777~
LX*1~
SV2*0300*HC:81000*120*UN*1~
DTP*472*D8*20100730~
LX*2~
SV2*0320*HC:76092*50*UN*1~
DTP*472*D8*20100730~
LX*3~
SV2*0270*HC:J1120*30*UN*1~
DTP*472*D8*20100730~
SE*38*0034~
GE*1*30~
IEA*1*000000031~
`);

const riskProfileBundle = {
  "resourceType": "Bundle",
  "type": "searchset",
  "entry": [
    {
      "resource": {
        "resourceType": "Patient",
        "id": "9cee689b-6501-4349-af32-e6849e179a2f",
        "meta": {
          "lastUpdated": "2023-02-22T11:27:29.9499804+00:00",
          "profile": [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
            "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-Patient"
          ]
        },
        "extension": [
          {
            "url": "http://hl7.org/fhir/StructureDefinition/patient-religion",
            "valueCodeableConcept": {
              "coding": [
                {
                  "system": "urn:oid:1.2.3.4.5.1.1",
                  "code": "Example",
                  "display": "Example",
                  "userSelected": true
                }
              ]
            }
          },
          {
            "extension": [
              {
                "url": "text",
                "valueString": "N"
              }
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
          },
          {
            "extension": [
              {
                "url": "text",
                "valueString": "Black"
              },
              {
                "url": "detailed",
                "valueCoding": {
                  "system": "urn:oid:2.16.840.1.113883.6.238",
                  "code": "2056-0",
                  "display": "BLACK",
                  "userSelected": false
                }
              }
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
          }
        ],
        "identifier": [
          {
            "use": "usual",
            "type": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                  "code": "MR"
                }
              ]
            },
            "system": "http://test.careevolution.com/identifiers/CareEvolution/MRN/1.2.3.4.5.1.7_1.2.3.4.5.1.7",
            "value": "0i56756845575l8yw6u886k4"
          },
          {
            "system": "http://test.careevolution.com/identifiers/1.2.3.4.5.1.7/1.2.3.4.5.1.7",
            "value": "0i56756845575l8yw6u886k4"
          },
          {
            "system": "http://test.careevolution.com/identifiers/1.2.3.4.5.1.7/1.3.6.1.4.1.5641",
            "value": "46274464"
          }
        ],
        "name": [
          {
            "use": "official",
            "_use": {
              "extension": [
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "http://careevolution.com/fhircodes#NameType",
                        "code": "LegalName",
                        "display": "Legal Name",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            },
            "family": "Tester",
            "given": [
              "Brittany"
            ]
          },
          {
            "_use": {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                  "valueCode": "unsupported"
                },
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "http://careevolution.com/fhircodes#NameType",
                        "code": "P",
                        "display": "Pseudonym",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            },
            "family": "Tester",
            "given": [
              "Brittany"
            ]
          }
        ],
        "telecom": [
          {
            "system": "phone",
            "_system": {
              "extension": [
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "http://careevolution.com/fhircodes#ContactInfoType",
                        "code": "HomePhone",
                        "display": "Home Phone",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            },
            "value": "tel:(680)555-1234",
            "use": "home",
            "_use": {
              "extension": [
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "urn:oid:1.2.3.4.5.1.7",
                        "code": "HP",
                        "display": "primary home",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "system": "phone",
            "_system": {
              "extension": [
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "http://careevolution.com/fhircodes#ContactInfoType",
                        "code": "OfficePhone",
                        "display": "Office Phone",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            },
            "value": "tel:(548)555-8765",
            "use": "work",
            "_use": {
              "extension": [
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "urn:oid:1.2.3.4.5.1.7",
                        "code": "WP",
                        "display": "work place",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "_system": {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                  "valueCode": "unsupported"
                },
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "urn:oid:1.2.3.4.5.1.7",
                        "code": "MC",
                        "display": "mobile contact",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            },
            "value": "tel:(574)555-3737"
          },
          {
            "_system": {
              "extension": [
                {
                  "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                  "valueCode": "unsupported"
                },
                {
                  "url": "http://careevolution.com/fhirextensions#term",
                  "valueCodeableConcept": {
                    "coding": [
                      {
                        "system": "urn:oid:1.2.3.4.5.1.7",
                        "code": "Other",
                        "display": "Other",
                        "userSelected": true
                      }
                    ]
                  }
                }
              ]
            },
            "value": "tel:(189)555-333"
          }
        ],
        "gender": "male",
        "_gender": {
          "extension": [
            {
              "url": "http://careevolution.com/fhirextensions#term",
              "valueCodeableConcept": {
                "coding": [
                  {
                    "system": "urn:oid:2.16.840.1.113883.5.1",
                    "code": "M",
                    "display": "Male",
                    "userSelected": true
                  },
                  {
                    "system": "http://careevolution.com",
                    "code": "M",
                    "display": "Male",
                    "userSelected": false
                  },
                  {
                    "system": "http://test.careevolution.com/codes/FhirCodesAlternate1/Gender",
                    "code": "M",
                    "display": "M",
                    "userSelected": false
                  },
                  {
                    "system": "http://hl7.org/fhir/v3/AdministrativeGender",
                    "code": "M",
                    "display": "Male",
                    "userSelected": false
                  },
                  {
                    "system": "http://hl7.org/fhir/administrative-gender",
                    "code": "male",
                    "display": "male",
                    "userSelected": false
                  },
                  {
                    "system": "http://test.careevolution.com/codes/FhirCodes/Gender",
                    "code": "male",
                    "userSelected": false
                  }
                ]
              }
            }
          ]
        },
        "birthDate": "1948-12-17",
        "deceasedBoolean": false,
        "address": [
          {
            "use": "home",
            "line": [
              "2608 Main Street"
            ],
            "city": "Anytown",
            "state": "MI",
            "postalCode": "48761"
          }
        ],
        "maritalStatus": {
          "coding": [
            {
              "system": "urn:oid:1.2.3.4.5.1.1",
              "code": "M",
              "display": "M",
              "userSelected": true
            }
          ]
        },
        "communication": [
          {
            "language": {
              "coding": [
                {
                  "system": "urn:oid:1.2.3.4.5.1.7",
                  "code": "ENGLISH",
                  "display": "ENGLISH",
                  "userSelected": true
                }
              ]
            },
            "preferred": true
          }
        ]
      }
    }
  ]
} as Bundle;

describe("classify condition", () => {
  it("should classify with URL", async () => {
    const result = await orchestrate.classifyCondition({
      code: "119981000146107",
      system: "http://snomed.info/sct",
    });
    expect(result).toBeDefined();
    expect(result.cciAcute).toBeTruthy();
  });

  it("should classify with name", async () => {
    const result = await orchestrate.classifyCondition({
      code: "119981000146107",
      system: "SNOMED",
    });
    expect(result).toBeDefined();
    expect(result.cciAcute).toBeTruthy();
  });
});

describe("classify medication", () => {
  it("should classify with URL", async () => {
    const result = await orchestrate.classifyMedication({
      "code": "2468231",
      "system": "http://www.nlm.nih.gov/research/umls/rxnorm"
    });
    expect(result).toBeDefined();
    expect(result.rxNormGeneric).toBeTruthy();
  });

  it("should classify with name", async () => {
    const result = await orchestrate.classifyMedication({
      "code": "2468231",
      "system": "RxNorm"
    });
    expect(result).toBeDefined();
    expect(result.rxNormGeneric).toBeTruthy();
  });
});

describe("classify observation", () => {
  it("should classify with URL", async () => {
    const result = await orchestrate.classifyObservation({
      "code": "94558-4",
      "system": "http://loinc.org"
    });
    expect(result).toBeDefined();
    expect(result.loincClass).toBe("MICRO");
  });

  it("should classify with name", async () => {
    const result = await orchestrate.classifyObservation({
      "code": "94558-4",
      "system": "LOINC"
    });
    expect(result).toBeDefined();
    expect(result.loincClass).toBe("MICRO");
  });
});

describe("standardize condition", () => {
  it("should standardize snomed", async () => {
    const result = await orchestrate.standardizeCondition({
      "code": "370221004"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("370221004");
  });

  it("should standardize icd", async () => {
    const result = await orchestrate.standardizeCondition({
      "code": "J45.50"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("J45.50");
  });

  it("should standardize free text", async () => {
    const result = await orchestrate.standardizeCondition({
      "display": "dm2"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "code": "44054006",
      "display": "Diabetes mellitus type 2 (disorder)",
      "system": "http://snomed.info/sct"
    });
  });
});

describe("standardize lab", () => {
  it("should standardize loinc", async () => {
    const result = await orchestrate.standardizeLab({
      "code": "4548-4"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("4548-4");
  });

  it("should standardize free text", async () => {
    const result = await orchestrate.standardizeLab({
      "display": "hba1c 1/15/22 from outside lab"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "system": "http://snomed.info/sct",
      "code": "43396009",
      "display": "Hemoglobin A1c measurement (procedure)"
    });
  });
});

describe("standardize medication", () => {
  it("should standardize rxnorm with system", async () => {
    const result = await orchestrate.standardizeMedication({
      "code": "861004",
      "system": "RxNorm"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("861004");
  });

  it("should standardize ndc", async () => {
    const result = await orchestrate.standardizeMedication({
      "code": "59267-1000-02",
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "system": "http://hl7.org/fhir/sid/ndc",
      "code": "59267100002",
      "display": "SARS-CoV-2 (COVID-19) vaccine, mRNA-BNT162b2 0.1 MG/ML Injectable Suspension"
    });
  });

  it("should standardize free text", async () => {
    const result = await orchestrate.standardizeMedication({
      "display": "Jentadueto extended (linagliptin 2.5 / metFORMIN  1000mg)"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
      "code": "1796093",
      "display": "linagliptin 2.5 MG / metformin hydrochloride 1000 MG Extended Release Oral Tablet [Jentadueto]"
    });
  });
});

describe("standardize observation", () => {
  it("should standardize loinc", async () => {
    const result = await orchestrate.standardizeObservation({
      "code": "8480-6"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("8480-6");
  });

  it("should standardize free text", async () => {
    const result = await orchestrate.standardizeObservation({
      "display": "BMI"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "system": "http://loinc.org",
      "code": "39156-5",
      "display": "BMI"
    });
  });
});

describe("standardize procedure", () => {
  it("should standardize snomed", async () => {
    const result = await orchestrate.standardizeProcedure({
      "code": "80146002"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("80146002");
  });

  it("should standardize free text", async () => {
    const result = await orchestrate.standardizeProcedure({
      "display": "ct head&neck"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "system": "http://snomed.info/sct",
      "code": "429858000",
      "display": "Computed tomography of head and neck (procedure)"
    });
  });
});

describe("standardize radiology", () => {
  it("should standardize snomed", async () => {
    const result = await orchestrate.standardizeRadiology({
      "code": "711232001",
      "system": "SNOMED"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding[0].code).toBe("711232001");
  });

  it("should standardize free text", async () => {
    const result = await orchestrate.standardizeRadiology({
      "display": "CT scan of head w/o iv contrast 3d ago@StJoes"
    });
    expect(result).toBeDefined();
    expect(result.coding.length).toBeGreaterThan(0);
    expect(result.coding).toContainEqual({
      "system": "http://loinc.org",
      "code": "30799-1",
      "display": "CT Head WO contr"
    });
  });
});

describe("convert hl7 to fhir r4", () => {
  it("should convert hl7", async () => {
    const result = await orchestrate.convertHl7ToFhirR4({
      hl7Message: hl7
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should convert hl7 with patient", async () => {
    const result = await orchestrate.convertHl7ToFhirR4({
      hl7Message: hl7,
      patientID: "1234"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});


describe("convert cda to fhir r4", () => {
  it("should convert cda", async () => {
    const result = await orchestrate.convertCdaToFhirR4({
      cda: cda
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should convert cda with patient", async () => {
    const result = await orchestrate.convertCdaToFhirR4({
      cda: cda,
      patientID: "1234"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});


describe("convert cda to pdf", () => {
  it("should convert cda", async () => {
    const result = await orchestrate.convertCdaToPdf({
      cda: cda
    });
    expect(result).toBeDefined();
    expect(result).toContain("%PDF");
  });
});

describe("convert fhir r4 to cda", () => {
  it("should convert fhir", async () => {
    const result = await orchestrate.convertFhirR4ToCda({
      fhirBundle: fhir
    });
    expect(result).toBeDefined();
    expect(result).toContain("<?xml");
  });
});

describe("convert fhir r4 to omop", () => {
  it("should convert fhir", async () => {
    const result = await orchestrate.convertFhirR4ToOmop({
      fhirBundle: fhir
    });
    expect(result).toBeDefined();
    expect(result).toContain("PROCESSING_LOG.csv");
  });
});

describe("convert x12 to fhir r4", () => {
  it("should convert x12", async () => {
    const result = await orchestrate.convertX12ToFhirR4({
      x12Document: x12Document
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should convert x12 with patient", async () => {
    const result = await orchestrate.convertX12ToFhirR4({
      x12Document: x12Document,
      patientID: "1234"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});

describe("insight risk profile", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.insightRiskProfile({
      hccVersion: "22",
      periodEndDate: "2020-12-31",
      raSegment: "community nondual aged",
      fhirBundle: riskProfileBundle,
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });
});

describe("get fhir r4 code system", () => {
  it("should return a code_system", async () => {
    const result = await orchestrate.getFhirR4CodeSystem({
      codeSystem: "SNOMED"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.concept?.length).toBeGreaterThan(0);
  }, 10000);

  it("should return a bundle with page", async () => {
    const result = await orchestrate.getFhirR4CodeSystem({
      codeSystem: "SNOMED",
      pageNumber: 1,
      pageSize: 2
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.concept?.length).toBe(2);
  });
});

describe("summarize fhir r4 code systems", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.summarizeFhirR4CodeSystems();
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });
});

describe("get fhir r4 concept maps", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.getFhirR4ConceptMaps();
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    expect(result.entry?.[0].resource?.resourceType).toBe("ConceptMap");
  });
});

describe("translate fhir r4 concept map", () => {
  it("should translate code", async () => {
    const result = await orchestrate.translateFhirR4ConceptMap({
      code: "119981000146107",
    });
    expect(result).toBeDefined();
    expect(result.parameter?.length).toBeGreaterThan(0);
  });

  it("should translate code and system", async () => {
    const result = await orchestrate.translateFhirR4ConceptMap({
      code: "119981000146107",
      domain: "Condition"
    });
    expect(result).toBeDefined();
    expect(result.parameter?.length).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 value set scope", () => {
  it("should return a bundle", async () => {
    const result = await orchestrate.summarizeFhirR4ValueSetScope({
      scope: "http://loinc.org"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  }, 10000);
});


describe("get fhir r4 value set", () => {
  it("should return a value set", async () => {
    const result = await orchestrate.getFhirR4ValueSet({
      id: "00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("ValueSet");
    expect(result.compose?.include?.length).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 value set", () => {
  it("should return a value set", async () => {
    const result = await orchestrate.summarizeFhirR4ValueSet({
      id: "00987FA2EDADBD0E43DA59E171B80F99DBF832C69904489EE6F9E6450925E5A2",
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("ValueSet");
  });
});

describe("get fhir r4 value set scopes", () => {
  it("should return a value set", async () => {
    const result = await orchestrate.getFhirR4ValueSetScopes();
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("ValueSet");
    expect(result.compose?.include.length).toBeGreaterThan(0);
  });
});

describe("get fhir r4 value set by scope", () => {
  it("should throw without pagination", async () => {
    await expect(orchestrate.getFhirR4ValueSetsByScope({
      scope: "http://loinc.org",
    })).rejects.toThrow();
  });

  it("should return a bundle with page and scope", async () => {
    const result = await orchestrate.getFhirR4ValueSetsByScope({
      scope: "http://loinc.org",
      pageNumber: 1,
      pageSize: 2
    });
    console.log(result.entry?.[0].resource);
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });

  it("should return a bundle with page and name", async () => {
    const result = await orchestrate.getFhirR4ValueSetsByScope({
      name: "LP7839-6",
      pageNumber: 1,
      pageSize: 2
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });

  it("should return a bundle with page, name, and scope", async () => {
    const result = await orchestrate.getFhirR4ValueSetsByScope({
      name: "LP7839-6",
      scope: "http://loinc.org",
      pageNumber: 1,
      pageSize: 2
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });

  it("should return a bundle with just page", async () => {
    const result = await orchestrate.getFhirR4ValueSetsByScope({
      pageNumber: 1,
      pageSize: 2
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.total).toBeGreaterThan(0);
  });
});

describe("summarize fhir r4 code system", () => {
  it("should return a code system", async () => {
    const result = await orchestrate.summarizeFhirR4CodeSystem({
      codeSystem: "SNOMED"
    });
    expect(result).toBeDefined();
    expect(result.resourceType).toBe("CodeSystem");
    expect(result.count).toBeGreaterThan(0);
  });
});

describe("get all fhir r4 value sets for codes", () => {
  it("should return parameters", async () => {
    const result = await orchestrate.getAllFhirR4ValueSetsForCodes({
      resourceType: "Parameters",
      parameter: [
        {
          name: "code",
          valueString: "119981000146107"
        },
        {
          name: "system",
          valueString: "http://snomed.info/sct"
        }
      ]
    });
    expect(result).toBeDefined();
    expect(result.parameter?.length).toBeGreaterThan(0);
  });
});

describe("convert combined fhir r4 bundles", () => {
  it("should combine", async () => {
    const bundles = (`
${JSON.stringify(fhir)}
${JSON.stringify(fhir)}
`);

    const result = await orchestrate.convertCombinedFhirR4Bundles({
      fhirBundles: bundles
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
  });

  it("should combine with patient", async () => {
    const bundles = (`
${JSON.stringify(fhir)}
${JSON.stringify(fhir)}
`);

    const result = await orchestrate.convertCombinedFhirR4Bundles({
      fhirBundles: bundles,
      personID: "1234"
    });

    expect(result).toBeDefined();
    expect(result.resourceType).toBe("Bundle");
    expect(result.entry?.length).toBeGreaterThan(0);
    const patientResource = result.entry?.find((entry) => entry.resource?.resourceType === "Patient");
    expect(patientResource).toBeDefined();
    expect(patientResource?.resource?.id).toBe("1234");
  });
});