from orchestrate._internal.fhir import Bundle


R4_BUNDLE = {
    "resourceType": "Bundle",
    "type": "batch-response",
    "entry": [
        {
            "fullUrl": "https://api.careevolutionapi.com/Patient/35b77437-425d-419c-90b5-af4bc433ebe9",
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
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "IheTestPatient",
                    },
                    {
                        "system": "http://rosetta.careevolution.com/identifiers/Proprietary/1.3.6.1.4.1.37608",
                        "value": "IheTestPatient",
                    },
                ],
                "name": [{"use": "official", "family": "Smith", "given": ["Patient"]}],
                "telecom": [
                    {"system": "phone", "value": "534-555-6666", "use": "home"}
                ],
                "gender": "female",
                "birthDate": "1956-08-13",
                "deceasedBoolean": False,
                "address": [
                    {
                        "use": "home",
                        "line": ["34 Drury Lane"],
                        "city": "Disney Land",
                        "state": "CA",
                        "postalCode": "90210",
                    }
                ],
            },
        }
    ],
}


CDA = """
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
"""


HL7 = """
MSH|^~\&|LAB|MYFAC|LAB||201411130917||ORU^R01|3216598|D|2.3|||AL|NE|
PID|1|ABC123DF|AND234DA_PID3|PID_4_ALTID|Smith^Patient^M||19670202 |F|||2222 22 st^^LAKE COUNTRY^NY^22222||222-222-2222|||||7890|
PV1|1|O|MYFACSOMPL||||^Smith^Patient^^^^^XAVS|||||||||||REF||SELF|||||||||||||||||||MYFAC||REG|||201411071440||||||||23390^PV1_52Smith^PV1_52Patient^H^^Dr^^PV1_52Mnemonic|
ORC|RE|PT103933301.0100|||CM|N|||201411130917|^John^Doctor^J.^^^^KYLA||^Smith^Patient^^^^^XAVS|MYFAC|
OBR|1|PT1311:H00001R301.0100|PT1311:H00001R|301.0100^Complete Blood Count (CBC)^00065227^57021-8^CBC \T\ Auto Differential^pCLOCD|R||201411130914|||KYLA||||201411130914||^Smith^Patient^^^^^XAVS||00065227||||201411130915||LAB|F||^^^^^R|^Smith^Patient^^^^^XAVS|
OBX|1|NM|301.0500^White Blood Count (WBC)^00065227^6690-2^Leukocytes^pCLOCD|1|10.1|10\S\9/L|3.1-9.7|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|2|NM|301.0600^Red Blood Count (RBC)^00065227^789-8^Erythrocytes^pCLOCD|1|3.2|10\S\12/L|3.7-5.0|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|3|NM|301.0700^Hemoglobin (HGB)^00065227^718-7^Hemoglobin^pCLOCD|1|140|g/L|118-151|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|4|NM|301.0900^Hematocrit (HCT)^00065227^4544-3^Hematocrit^pCLOCD|1|0.34|L/L|0.33-0.45|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|5|NM|301.1100^MCV^00065227^787-2^Mean Corpuscular Volume^pCLOCD|1|98.0|fL|84.0-98.0|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|6|NM|301.1300^MCH^00065227^785-6^Mean Corpuscular Hemoglobin^pCLOCD|1|27.0|pg|28.3-33.5|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|7|NM|301.1500^MCHC^00065227^786-4^Mean Corpuscular Hemoglobin Concentration^pCLOCD|1|330|g/L|329-352|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|8|NM|301.1700^RDW^00065227^788-0^Erythrocyte Distribution Width^pCLOCD|1|12.0|%|12.0-15.0|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|9|NM|301.1900^Platelets^00065227^777-3^Platelets^pCLOCD|1|125|10\S\9/L|147-375|L||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|10|NM|301.2100^Neutrophils^00065227^751-8^Neutrophils^pCLOCD|1|8.0|10\S\9/L|1.2-6.0|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|11|NM|301.2300^Lymphocytes^00065227^731-0^Lymphocytes^pCLOCD|1|1.0|10\S\9/L|0.6-3.1|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|12|NM|301.2500^Monocytes^00065227^742-7^Monocytes^pCLOCD|1|1.0|10\S\9/L|0.1-0.9|H||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|13|NM|301.2700^Eosinophils^00065227^711-2^Eosinophils^pCLOCD|1|0.0|10\S\9/L|0.0-0.5|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
OBX|14|NM|301.2900^Basophils^00065227^704-7^Basophils^pCLOCD|1|0.0|10\S\9/L|0.0-0.2|N||A~S|F|||201411130916|MYFAC^MyFake Hospital^L|
ZDR||^Smith^Patient^^^^^XAVS^^^^^XX^^ATP|
ZPR||
"""


RISK_PROFILE_BUNDLE = {
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
                        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-Patient",
                    ],
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
                                    "userSelected": True,
                                }
                            ]
                        },
                    },
                    {
                        "extension": [{"url": "text", "valueString": "N"}],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
                    },
                    {
                        "extension": [
                            {"url": "text", "valueString": "Black"},
                            {
                                "url": "detailed",
                                "valueCoding": {
                                    "system": "urn:oid:2.16.840.1.113883.6.238",
                                    "code": "2056-0",
                                    "display": "BLACK",
                                    "userSelected": False,
                                },
                            },
                        ],
                        "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
                    },
                ],
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "http://test.careevolution.com/identifiers/CareEvolution/MRN/1.2.3.4.5.1.7_1.2.3.4.5.1.7",
                        "value": "0i56756845575l8yw6u886k4",
                    },
                    {
                        "system": "http://test.careevolution.com/identifiers/1.2.3.4.5.1.7/1.2.3.4.5.1.7",
                        "value": "0i56756845575l8yw6u886k4",
                    },
                    {
                        "system": "http://test.careevolution.com/identifiers/1.2.3.4.5.1.7/1.3.6.1.4.1.5641",
                        "value": "46274464",
                    },
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
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                        "family": "Tester",
                        "given": ["Brittany"],
                    },
                    {
                        "_use": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                    "valueCode": "unsupported",
                                },
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "http://careevolution.com/fhircodes#NameType",
                                                "code": "P",
                                                "display": "Pseudonym",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                },
                            ]
                        },
                        "family": "Tester",
                        "given": ["Brittany"],
                    },
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
                                                "userSelected": True,
                                            }
                                        ]
                                    },
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
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
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
                                                "userSelected": True,
                                            }
                                        ]
                                    },
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
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                    },
                    {
                        "_system": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                    "valueCode": "unsupported",
                                },
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "urn:oid:1.2.3.4.5.1.7",
                                                "code": "MC",
                                                "display": "mobile contact",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                },
                            ]
                        },
                        "value": "tel:(574)555-3737",
                    },
                    {
                        "_system": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                                    "valueCode": "unsupported",
                                },
                                {
                                    "url": "http://careevolution.com/fhirextensions#term",
                                    "valueCodeableConcept": {
                                        "coding": [
                                            {
                                                "system": "urn:oid:1.2.3.4.5.1.7",
                                                "code": "Other",
                                                "display": "Other",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                },
                            ]
                        },
                        "value": "tel:(189)555-333",
                    },
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
                                        "userSelected": True,
                                    },
                                    {
                                        "system": "http://careevolution.com",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://test.careevolution.com/codes/FhirCodesAlternate1/Gender",
                                        "code": "M",
                                        "display": "M",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/v3/AdministrativeGender",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/administrative-gender",
                                        "code": "male",
                                        "display": "male",
                                        "userSelected": False,
                                    },
                                    {
                                        "system": "http://test.careevolution.com/codes/FhirCodes/Gender",
                                        "code": "male",
                                        "userSelected": False,
                                    },
                                ]
                            },
                        }
                    ]
                },
                "birthDate": "1948-12-17",
                "deceasedBoolean": False,
                "address": [
                    {
                        "use": "home",
                        "line": ["2608 Main Street"],
                        "city": "Anytown",
                        "state": "MI",
                        "postalCode": "48761",
                    }
                ],
                "maritalStatus": {
                    "coding": [
                        {
                            "system": "urn:oid:1.2.3.4.5.1.1",
                            "code": "M",
                            "display": "M",
                            "userSelected": True,
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
                                    "userSelected": True,
                                }
                            ]
                        },
                        "preferred": True,
                    }
                ],
            }
        }
    ],
}

DSTU2_BUNDLE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "entry": [
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
            "resource": {
                "resourceType": "Patient",
                "id": "3ead5e15-4da5-480b-8a94-ffea1e936809",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T15:08:05.723+00:00",
                    "profile": [
                        "http://fhir.org/guides/argonaut/StructureDefinition/argo-patient"
                    ],
                    "security": [
                        {
                            "system": "http://careevolution.com/accesspolicyname",
                            "code": "Standard Record Policy",
                        }
                    ],
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#patientInstitutions",
                        "valueCoding": {
                            "id": "patient-institution1",
                            "code": "BeaconInstitution",
                            "display": "BeaconInstitution",
                        },
                    }
                ],
                "identifier": [
                    {
                        "id": "id1",
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        "value": "12345A",
                    },
                    {
                        "id": "id2",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN",
                        "value": "12345A",
                    },
                    {
                        "id": "id3",
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                ],
                "name": [
                    {
                        "id": "name1",
                        "use": "official",
                        "family": ["Smith"],
                        "given": ["John"],
                    }
                ],
                "gender": "male",
                "_gender": {
                    "id": "gender1",
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "id": "gender2",
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/CareEvolution/Gender",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": True,
                                    }
                                ],
                            },
                        }
                    ],
                },
                "birthDate": "1961-01-14",
                "_birthDate": {"id": "birthdate1"},
                "deceasedBoolean": False,
                "_deceasedBoolean": {"id": "deceased1"},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/0-3a4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "0-3a4295efae7fed11b9cc0e32e07a5c1b",
                "contained": [
                    {
                        "resourceType": "Patient",
                        "id": "patient",
                        "meta": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                                    "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                                }
                            ],
                            "profile": [
                                "http://fhir.org/guides/argonaut/StructureDefinition/argo-patient"
                            ],
                            "security": [
                                {
                                    "system": "http://careevolution.com/accesspolicyname",
                                    "code": "Standard Record Policy",
                                }
                            ],
                        },
                        "extension": [
                            {
                                "url": "http://careevolution.com/fhirextensions#patientInstitutions",
                                "valueCoding": {
                                    "id": "patient-institution1",
                                    "code": "BeaconInstitution",
                                    "display": "BeaconInstitution",
                                },
                            }
                        ],
                        "identifier": [
                            {
                                "use": "usual",
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "MR",
                                        }
                                    ]
                                },
                                "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                                "value": "12345A",
                            },
                            {
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "MR",
                                        }
                                    ]
                                },
                                "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN",
                                "value": "12345A",
                            },
                            {
                                "system": "http://careevolution.com/fhir/PatientId",
                                "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                            },
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
                                                        "system": "http://fhir.carevolution.com/codes/CareEvolution/NameType",
                                                        "code": "LegalName",
                                                        "display": "Legal Name",
                                                        "userSelected": True,
                                                    }
                                                ]
                                            },
                                        }
                                    ]
                                },
                                "family": ["Smith"],
                                "given": ["John"],
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
                                                "system": "http://fhir.carevolution.com/codes/CareEvolution/Gender",
                                                "code": "M",
                                                "display": "Male",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                        "birthDate": "1961-01-14",
                        "deceasedBoolean": False,
                    }
                ],
                "target": [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#id1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#id2",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#id3",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#name1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#birthdate1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#deceased1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#gender1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#gender2",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#patient-institution1",
                            },
                        ],
                        "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    }
                ],
                "period": {
                    "start": "2022-12-19T15:08:05.723+00:00",
                    "end": "2022-12-19T15:08:05.717+00:00",
                },
                "recorded": "2022-12-19T15:08:05.717+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "UPDATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
                "entity": [
                    {
                        "role": "source",
                        "type": {
                            "system": "http://hl7.org/fhir/resource-types",
                            "code": "Patient",
                        },
                        "reference": "#patient",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Condition/5.d30a4c15f97fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Condition",
                "id": "5.d30a4c15f97fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T23:58:55.387+00:00",
                },
                "patient": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisCode",
                            "code": "flu",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "6142004",
                            "display": "Influenza (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "J11.1",
                            "display": "Influenza due to unidentified influenza virus with other respiratory manifestations",
                            "userSelected": False,
                        },
                    ]
                },
                "category": {
                    "coding": [
                        {"system": "http://argonaut.hl7.org", "code": "health-concern"},
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisType",
                            "code": "EncounterDiagnosis",
                            "userSelected": True,
                        },
                        {
                            "system": "http://fhir.carevolution.com/codes/fhir-diagnosis-role/Reference",
                            "code": "CC",
                            "display": "Chief complaint",
                            "userSelected": False,
                        },
                    ]
                },
                "clinicalStatus": "resolved",
                "_clinicalStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisStatus",
                                        "code": "resolved",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "_verificationStatus": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                            "valueCode": "unsupported",
                        },
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisVerificationStatus",
                                        "code": "unconfirmed",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                    ]
                },
                "onsetDateTime": "2022-12-19T02:31:55.382-05:00",
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Condition/5.3d4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Condition",
                "id": "5.3d4295efae7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T15:08:05.75+00:00",
                    "profile": [
                        "http://fhir.org/guides/argonaut/StructureDefinition/argo-condition"
                    ],
                },
                "patient": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisCode",
                            "code": "multiple sclerosis",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "24700007",
                            "display": "Multiple sclerosis (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "G35",
                            "display": "Multiple sclerosis",
                            "userSelected": False,
                        },
                    ]
                },
                "category": {
                    "coding": [
                        {"system": "http://argonaut.hl7.org", "code": "health-concern"},
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisType",
                            "code": "EncounterDiagnosis",
                            "userSelected": True,
                        },
                        {
                            "system": "http://fhir.carevolution.com/codes/fhir-diagnosis-role/Reference",
                            "code": "CC",
                            "display": "Chief complaint",
                            "userSelected": False,
                        },
                    ]
                },
                "clinicalStatus": "resolved",
                "_clinicalStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisStatus",
                                        "code": "inactive",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "verificationStatus": "confirmed",
                "_verificationStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisVerificationStatus",
                                        "code": "confirmed",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "onsetDateTime": "2022-12-18T18:55:05.675-05:00",
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Condition/5.3c4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Condition",
                "id": "5.3c4295efae7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T15:08:05.74+00:00",
                },
                "patient": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisCode",
                            "code": "crohns disease",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "34000006",
                            "display": "Crohn's disease (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "K50.90",
                            "display": "Crohn's disease, unspecified, without complications",
                            "userSelected": False,
                        },
                    ]
                },
                "category": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                            "valueCode": "unsupported",
                        }
                    ],
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisType",
                            "code": "SECONDARY",
                            "display": "SECONDARY",
                            "userSelected": True,
                        },
                        {
                            "system": "http://fhir.carevolution.com/codes/CareEvolution/DiagnosisType",
                            "code": "Secondary",
                            "display": "Secondary",
                            "userSelected": False,
                        },
                    ],
                },
                "clinicalStatus": "active",
                "_clinicalStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisStatus",
                                        "code": "Active",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "verificationStatus": "confirmed",
                "_verificationStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisVerificationStatus",
                                        "code": "confirmed",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "onsetDateTime": "2022-12-18T17:20:05.675-05:00",
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/4-d30a4c15f97fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "4-d30a4c15f97fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Condition/5.d30a4c15f97fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T23:58:55.387+00:00",
                    "end": "2022-12-19T23:58:55.387+00:00",
                },
                "recorded": "2022-12-19T23:58:55.387+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/4-3d4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "4-3d4295efae7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Condition/5.3d4295efae7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T15:08:05.75+00:00",
                    "end": "2022-12-19T15:08:05.75+00:00",
                },
                "recorded": "2022-12-19T15:08:05.75+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/4-3c4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "4-3c4295efae7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Condition/5.3c4295efae7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T15:08:05.74+00:00",
                    "end": "2022-12-19T15:08:05.74+00:00",
                },
                "recorded": "2022-12-19T15:08:05.74+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.682d4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.682d4f56bc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:44:05.61+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-18T13:45:05.605-05:00",
                "issued": "2022-12-18T13:45:05.605-05:00",
                "valueQuantity": {"value": 1690728474},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.d12b4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.d12b4f56bc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:44:03.04+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-18T14:56:03.025-05:00",
                "issued": "2022-12-18T14:56:03.025-05:00",
                "valueQuantity": {"value": 1271126762},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.028d6f3ebc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.028d6f3ebc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:43:26.953+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-18T17:09:26.943-05:00",
                "issued": "2022-12-18T17:09:26.943-05:00",
                "valueQuantity": {"value": 295302631},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.54e37a32bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.54e37a32bc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:43:10.48+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-19T10:31:10.464-05:00",
                "issued": "2022-12-19T10:31:10.464-05:00",
                "valueQuantity": {"value": 652309659},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.d24b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.d24b67f6bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:41:23.93+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-18T11:44:23.919-05:00",
                "issued": "2022-12-18T11:44:23.919-05:00",
                "valueQuantity": {"value": 789662810},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.a94b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.a94b67f6bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:41:22.403+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-18T11:56:22.403-05:00",
                "issued": "2022-12-18T11:56:22.403-05:00",
                "valueQuantity": {"value": 1582118206},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.f1b562d2bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.f1b562d2bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:40:27.56+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-18T22:38:27.543-05:00",
                "issued": "2022-12-18T22:38:27.543-05:00",
                "valueQuantity": {"value": 252600252},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.2d6720babb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.2d6720babb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-20T03:22:56.517+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-19T11:21:45.582-05:00",
                "issued": "2022-12-19T11:21:45.582-05:00",
                "valueQuantity": {"value": 1724700070},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.b185f6a7bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.b185f6a7bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:39:16.903+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-19T10:56:16.9-05:00",
                "issued": "2022-12-19T10:56:16.9-05:00",
                "valueQuantity": {"value": 2126651898},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.74ec7d5fbb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.74ec7d5fbb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:37:09.9+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-19T07:24:09.891-05:00",
                "issued": "2022-12-19T07:24:09.891-05:00",
                "valueQuantity": {"value": 941137949},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.1a5cf010bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.1a5cf010bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:35:02.83+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-19T10:44:02.819-05:00",
                "issued": "2022-12-19T10:44:02.819-05:00",
                "valueQuantity": {"value": 1868889329},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Observation/1.f59dca04bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.f59dca04bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:34:40.32+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809"
                },
                "effectiveDateTime": "2022-12-19T11:11:40.299-05:00",
                "issued": "2022-12-19T11:11:40.299-05:00",
                "valueQuantity": {"value": 1577878080},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-682d4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-682d4f56bc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.682d4f56bc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:44:05.61+00:00",
                    "end": "2022-12-19T16:44:05.61+00:00",
                },
                "recorded": "2022-12-19T16:44:05.61+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-d12b4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-d12b4f56bc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.d12b4f56bc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:44:03.04+00:00",
                    "end": "2022-12-19T16:44:03.04+00:00",
                },
                "recorded": "2022-12-19T16:44:03.04+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-028d6f3ebc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-028d6f3ebc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.028d6f3ebc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:43:26.953+00:00",
                    "end": "2022-12-19T16:43:26.953+00:00",
                },
                "recorded": "2022-12-19T16:43:26.953+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-54e37a32bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-54e37a32bc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.54e37a32bc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:43:10.48+00:00",
                    "end": "2022-12-19T16:43:10.48+00:00",
                },
                "recorded": "2022-12-19T16:43:10.48+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-d24b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-d24b67f6bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.d24b67f6bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:41:23.93+00:00",
                    "end": "2022-12-19T16:41:23.93+00:00",
                },
                "recorded": "2022-12-19T16:41:23.93+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-a94b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-a94b67f6bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.a94b67f6bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:41:22.403+00:00",
                    "end": "2022-12-19T16:41:22.403+00:00",
                },
                "recorded": "2022-12-19T16:41:22.403+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-f1b562d2bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-f1b562d2bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.f1b562d2bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:40:27.56+00:00",
                    "end": "2022-12-19T16:40:27.56+00:00",
                },
                "recorded": "2022-12-19T16:40:27.56+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-2d6720babb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-2d6720babb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.2d6720babb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:39:45.6+00:00",
                    "end": "2022-12-20T03:22:56.517+00:00",
                },
                "recorded": "2022-12-20T03:22:56.517+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "UPDATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-b185f6a7bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-b185f6a7bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.b185f6a7bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:39:16.903+00:00",
                    "end": "2022-12-19T16:39:16.903+00:00",
                },
                "recorded": "2022-12-19T16:39:16.903+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-74ec7d5fbb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-74ec7d5fbb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.74ec7d5fbb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:37:09.9+00:00",
                    "end": "2022-12-19T16:37:09.9+00:00",
                },
                "recorded": "2022-12-19T16:37:09.9+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-1a5cf010bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-1a5cf010bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.1a5cf010bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:35:02.83+00:00",
                    "end": "2022-12-19T16:35:02.83+00:00",
                },
                "recorded": "2022-12-19T16:35:02.83+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir/Provenance/17-f59dca04bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "17-f59dca04bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.f59dca04bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:34:40.32+00:00",
                    "end": "2022-12-19T16:34:40.32+00:00",
                },
                "recorded": "2022-12-19T16:34:40.32+00:00",
                "activity": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                            "code": "CREATE",
                        }
                    ]
                },
                "agent": [
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "author",
                        },
                        "actor": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "performer",
                        },
                        "actor": {"display": "Sweetriver"},
                        "userId": {
                            "use": "official",
                            "system": "http://fhir.carevolution.com/typeid/Application",
                            "value": "1",
                        },
                    },
                    {
                        "role": {
                            "system": "http://hl7.org/fhir/provenance-participant-role",
                            "code": "enterer",
                        },
                        "actor": {"display": "SystemUser"},
                        "userId": {
                            "system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                        },
                    },
                ],
            },
        },
    ],
}


X12_DOCUMENT = """ISA*00*          *00*          *ZZ*SUBMITTERID    *ZZ*RECEIVERID     *230616*1145*^*00501*000000001*0*T*:~
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
"""

STU3_BUNDLE = {
    "resourceType": "Bundle",
    "type": "searchset",
    "entry": [
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
            "resource": {
                "resourceType": "Patient",
                "id": "3ead5e15-4da5-480b-8a94-ffea1e936809",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T15:08:05.723+00:00",
                    "security": [
                        {
                            "system": "http://careevolution.com/accesspolicyname",
                            "code": "Standard Record Policy",
                        }
                    ],
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#patientInstitutions",
                        "valueCoding": {
                            "id": "patient-institution1",
                            "code": "BeaconInstitution",
                            "display": "BeaconInstitution",
                        },
                    }
                ],
                "identifier": [
                    {
                        "id": "id1",
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        "value": "1234A",
                    },
                    {
                        "id": "id2",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN",
                        "value": "1234A",
                    },
                    {
                        "id": "id3",
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                ],
                "name": [
                    {
                        "id": "name1",
                        "use": "official",
                        "family": "Smith",
                        "given": ["John"],
                    }
                ],
                "gender": "male",
                "_gender": {
                    "id": "gender1",
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "id": "gender2",
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/CareEvolution/Gender",
                                        "code": "M",
                                        "display": "Male",
                                        "userSelected": True,
                                    }
                                ],
                            },
                        }
                    ],
                },
                "birthDate": "1961-01-02",
                "_birthDate": {"id": "birthdate1"},
                "deceasedBoolean": False,
                "_deceasedBoolean": {"id": "deceased1"},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/0-3a4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "0-3a4295efae7fed11b9cc0e32e07a5c1b",
                "contained": [
                    {
                        "resourceType": "Patient",
                        "id": "patient",
                        "meta": {
                            "extension": [
                                {
                                    "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                                    "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                                }
                            ],
                            "security": [
                                {
                                    "system": "http://careevolution.com/accesspolicyname",
                                    "code": "Standard Record Policy",
                                }
                            ],
                        },
                        "extension": [
                            {
                                "url": "http://careevolution.com/fhirextensions#patientInstitutions",
                                "valueCoding": {
                                    "id": "patient-institution1",
                                    "code": "BeaconInstitution",
                                    "display": "BeaconInstitution",
                                },
                            }
                        ],
                        "identifier": [
                            {
                                "use": "usual",
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "MR",
                                        }
                                    ]
                                },
                                "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                                "value": "1234A",
                            },
                            {
                                "type": {
                                    "coding": [
                                        {
                                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                            "code": "MR",
                                        }
                                    ]
                                },
                                "system": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN",
                                "value": "1234A",
                            },
                            {
                                "system": "http://careevolution.com/fhir/PatientId",
                                "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                            },
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
                                                        "system": "http://fhir.carevolution.com/codes/CareEvolution/NameType",
                                                        "code": "LegalName",
                                                        "display": "Legal Name",
                                                        "userSelected": True,
                                                    }
                                                ]
                                            },
                                        }
                                    ]
                                },
                                "family": "Smith",
                                "given": ["John"],
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
                                                "system": "http://fhir.carevolution.com/codes/CareEvolution/Gender",
                                                "code": "M",
                                                "display": "Male",
                                                "userSelected": True,
                                            }
                                        ]
                                    },
                                }
                            ]
                        },
                        "birthDate": "1961-01-02",
                        "deceasedBoolean": False,
                    }
                ],
                "target": [
                    {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#id1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#id2",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#id3",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#name1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#birthdate1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#deceased1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#gender1",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#gender2",
                            },
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/targetElement",
                                "valueUri": "#patient-institution1",
                            },
                        ],
                        "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    }
                ],
                "period": {
                    "start": "2022-12-19T15:08:05.723+00:00",
                    "end": "2022-12-19T15:08:05.717+00:00",
                },
                "recorded": "2022-12-19T15:08:05.717+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "UPDATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
                "entity": [
                    {"role": "source", "whatReference": {"reference": "#patient"}}
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Condition/5.d30a4c15f97fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Condition",
                "id": "5.d30a4c15f97fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T23:58:55.387+00:00",
                },
                "clinicalStatus": "resolved",
                "_clinicalStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisStatus",
                                        "code": "resolved",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "_verificationStatus": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
                            "valueCode": "unsupported",
                        },
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisVerificationStatus",
                                        "code": "unconfirmed",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://hl7.org/fhir/condition-category",
                                "code": "encounter-diagnosis",
                            },
                            {
                                "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisType",
                                "code": "EncounterDiagnosis",
                                "userSelected": True,
                            },
                            {
                                "system": "http://fhir.carevolution.com/codes/fhir-diagnosis-role/Reference",
                                "code": "CC",
                                "display": "Chief complaint",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisCode",
                            "code": "flu",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "6142004",
                            "display": "Influenza (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "J11.1",
                            "display": "Influenza due to unidentified influenza virus with other respiratory manifestations",
                            "userSelected": False,
                        },
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "onsetDateTime": "2022-12-19T02:31:55.382-05:00",
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Condition/5.3d4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Condition",
                "id": "5.3d4295efae7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T15:08:05.75+00:00",
                },
                "clinicalStatus": "inactive",
                "_clinicalStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisStatus",
                                        "code": "inactive",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "verificationStatus": "confirmed",
                "_verificationStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisVerificationStatus",
                                        "code": "confirmed",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://hl7.org/fhir/condition-category",
                                "code": "encounter-diagnosis",
                            },
                            {
                                "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisType",
                                "code": "EncounterDiagnosis",
                                "userSelected": True,
                            },
                            {
                                "system": "http://fhir.carevolution.com/codes/fhir-diagnosis-role/Reference",
                                "code": "CC",
                                "display": "Chief complaint",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisCode",
                            "code": "multiple sclerosis",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "24700007",
                            "display": "Multiple sclerosis (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "G35",
                            "display": "Multiple sclerosis",
                            "userSelected": False,
                        },
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "onsetDateTime": "2022-12-18T18:55:05.675-05:00",
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Condition/5.3c4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Condition",
                "id": "5.3c4295efae7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T15:08:05.74+00:00",
                },
                "clinicalStatus": "active",
                "_clinicalStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisStatus",
                                        "code": "Active",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "verificationStatus": "confirmed",
                "_verificationStatus": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#term",
                            "valueCodeableConcept": {
                                "coding": [
                                    {
                                        "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisVerificationStatus",
                                        "code": "confirmed",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        }
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisType",
                                "code": "SECONDARY",
                                "display": "SECONDARY",
                                "userSelected": True,
                            },
                            {
                                "system": "http://fhir.carevolution.com/codes/CareEvolution/DiagnosisType",
                                "code": "Secondary",
                                "display": "Secondary",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/DiagnosisCode",
                            "code": "crohns disease",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "34000006",
                            "display": "Crohn's disease (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "K50.90",
                            "display": "Crohn's disease, unspecified, without complications",
                            "userSelected": False,
                        },
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "onsetDateTime": "2022-12-18T17:20:05.675-05:00",
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/4-d30a4c15f97fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "4-d30a4c15f97fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Condition/7.d30a4c15f97fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T23:58:55.387+00:00",
                    "end": "2022-12-19T23:58:55.387+00:00",
                },
                "recorded": "2022-12-19T23:58:55.387+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/4-3d4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "4-3d4295efae7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Condition/7.3d4295efae7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T15:08:05.75+00:00",
                    "end": "2022-12-19T15:08:05.75+00:00",
                },
                "recorded": "2022-12-19T15:08:05.75+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/4-3c4295efae7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "4-3c4295efae7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Condition/7.3c4295efae7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T15:08:05.74+00:00",
                    "end": "2022-12-19T15:08:05.74+00:00",
                },
                "recorded": "2022-12-19T15:08:05.74+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.682d4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.682d4f56bc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:44:05.61+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-18T13:45:05.605-05:00",
                "issued": "2022-12-18T13:45:05.605-05:00",
                "valueQuantity": {"value": 1690728474},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.d12b4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.d12b4f56bc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:44:03.04+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-18T14:56:03.025-05:00",
                "issued": "2022-12-18T14:56:03.025-05:00",
                "valueQuantity": {"value": 1271126762},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.028d6f3ebc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.028d6f3ebc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:43:26.953+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-18T17:09:26.943-05:00",
                "issued": "2022-12-18T17:09:26.943-05:00",
                "valueQuantity": {"value": 295302631},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.54e37a32bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.54e37a32bc7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:43:10.48+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-19T10:31:10.464-05:00",
                "issued": "2022-12-19T10:31:10.464-05:00",
                "valueQuantity": {"value": 652309659},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.d24b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.d24b67f6bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:41:23.93+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-18T11:44:23.919-05:00",
                "issued": "2022-12-18T11:44:23.919-05:00",
                "valueQuantity": {"value": 789662810},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.a94b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.a94b67f6bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:41:22.403+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-18T11:56:22.403-05:00",
                "issued": "2022-12-18T11:56:22.403-05:00",
                "valueQuantity": {"value": 1582118206},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.f1b562d2bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.f1b562d2bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:40:27.56+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-18T22:38:27.543-05:00",
                "issued": "2022-12-18T22:38:27.543-05:00",
                "valueQuantity": {"value": 252600252},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.2d6720babb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.2d6720babb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-20T03:22:56.517+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-19T11:21:45.582-05:00",
                "issued": "2022-12-19T11:21:45.582-05:00",
                "valueQuantity": {"value": 1724700070},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.b185f6a7bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.b185f6a7bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:39:16.903+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-19T10:56:16.9-05:00",
                "issued": "2022-12-19T10:56:16.9-05:00",
                "valueQuantity": {"value": 2126651898},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.74ec7d5fbb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.74ec7d5fbb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:37:09.9+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-19T07:24:09.891-05:00",
                "issued": "2022-12-19T07:24:09.891-05:00",
                "valueQuantity": {"value": 941137949},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.1a5cf010bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.1a5cf010bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:35:02.83+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-19T10:44:02.819-05:00",
                "issued": "2022-12-19T10:44:02.819-05:00",
                "valueQuantity": {"value": 1868889329},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Observation/1.f59dca04bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Observation",
                "id": "1.f59dca04bb7fed11b9cc0e32e07a5c1b",
                "meta": {
                    "extension": [
                        {
                            "url": "http://hl7.org/fhir/4.0/StructureDefinition/extension-meta.source",
                            "valueUri": "http://fhir.carevolution.com/identifiers/CareEvolution/MRN/problemSelectorTest",
                        }
                    ],
                    "lastUpdated": "2022-12-19T16:34:40.32+00:00",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-contextID",
                        "valueString": "f39dca04-bb7f-ed11-b9cc-0e32e07a5c1b",
                    }
                ],
                "status": "unknown",
                "code": {
                    "coding": [
                        {
                            "system": "http://fhir.carevolution.com/codes/DemoNamespace/ObservationType",
                            "code": "BeaconFakeObservation",
                            "userSelected": True,
                        }
                    ]
                },
                "subject": {
                    "reference": "Patient/3ead5e15-4da5-480b-8a94-ffea1e936809",
                    "identifier": {
                        "system": "http://careevolution.com/fhir/PatientId",
                        "value": "3a4295ef-ae7f-ed11-b9cc-0e32e07a5c1b",
                    },
                },
                "effectiveDateTime": "2022-12-19T11:11:40.299-05:00",
                "issued": "2022-12-19T11:11:40.299-05:00",
                "valueQuantity": {"value": 1577878080},
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-682d4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-682d4f56bc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.682d4f56bc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:44:05.61+00:00",
                    "end": "2022-12-19T16:44:05.61+00:00",
                },
                "recorded": "2022-12-19T16:44:05.61+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-d12b4f56bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-d12b4f56bc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.d12b4f56bc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:44:03.04+00:00",
                    "end": "2022-12-19T16:44:03.04+00:00",
                },
                "recorded": "2022-12-19T16:44:03.04+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-028d6f3ebc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-028d6f3ebc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.028d6f3ebc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:43:26.953+00:00",
                    "end": "2022-12-19T16:43:26.953+00:00",
                },
                "recorded": "2022-12-19T16:43:26.953+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-54e37a32bc7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-54e37a32bc7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.54e37a32bc7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:43:10.48+00:00",
                    "end": "2022-12-19T16:43:10.48+00:00",
                },
                "recorded": "2022-12-19T16:43:10.48+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-d24b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-d24b67f6bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.d24b67f6bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:41:23.93+00:00",
                    "end": "2022-12-19T16:41:23.93+00:00",
                },
                "recorded": "2022-12-19T16:41:23.93+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-a94b67f6bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-a94b67f6bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.a94b67f6bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:41:22.403+00:00",
                    "end": "2022-12-19T16:41:22.403+00:00",
                },
                "recorded": "2022-12-19T16:41:22.403+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-f1b562d2bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-f1b562d2bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.f1b562d2bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:40:27.56+00:00",
                    "end": "2022-12-19T16:40:27.56+00:00",
                },
                "recorded": "2022-12-19T16:40:27.56+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-2d6720babb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-2d6720babb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.2d6720babb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:39:45.6+00:00",
                    "end": "2022-12-20T03:22:56.517+00:00",
                },
                "recorded": "2022-12-20T03:22:56.517+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "UPDATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-b185f6a7bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-b185f6a7bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.b185f6a7bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:39:16.903+00:00",
                    "end": "2022-12-19T16:39:16.903+00:00",
                },
                "recorded": "2022-12-19T16:39:16.903+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-74ec7d5fbb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-74ec7d5fbb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.74ec7d5fbb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:37:09.9+00:00",
                    "end": "2022-12-19T16:37:09.9+00:00",
                },
                "recorded": "2022-12-19T16:37:09.9+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-1a5cf010bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-1a5cf010bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.1a5cf010bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:35:02.83+00:00",
                    "end": "2022-12-19T16:35:02.83+00:00",
                },
                "recorded": "2022-12-19T16:35:02.83+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
        {
            "fullUrl": "https://fhir.careevolution.com/Master.Adapter1.WebClient/api/fhir-stu3/Provenance/16-f59dca04bb7fed11b9cc0e32e07a5c1b",
            "resource": {
                "resourceType": "Provenance",
                "id": "16-f59dca04bb7fed11b9cc0e32e07a5c1b",
                "target": [
                    {"reference": "Observation/1.f59dca04bb7fed11b9cc0e32e07a5c1b"}
                ],
                "period": {
                    "start": "2022-12-19T16:34:40.32+00:00",
                    "end": "2022-12-19T16:34:40.32+00:00",
                },
                "recorded": "2022-12-19T16:34:40.32+00:00",
                "activity": {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-DataOperation",
                    "code": "CREATE",
                },
                "agent": [
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://hl7.org/fhir/v3/ParticipationType",
                                        "code": "AUT",
                                        "display": "Author (originator)",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "author",
                                    },
                                ],
                                "text": "Originating organization",
                            }
                        ],
                        "whoReference": {
                            "reference": "Organization/65db5f61-777c-ed11-b9cc-0e32e07a5c1b",
                            "display": "problemSelectorTest",
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://dicom.nema.org/resources/ontology/DCM",
                                        "code": "110150",
                                        "display": "Application",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "performer",
                                    },
                                ],
                                "text": "Application",
                            }
                        ],
                        "whoReference": {
                            "display": "Sweetriver",
                            "identifier": {
                                "use": "official",
                                "system": "http://fhir.carevolution.com/typeid/Application",
                                "value": "1",
                            },
                        },
                    },
                    {
                        "role": [
                            {
                                "coding": [
                                    {
                                        "system": "http://terminology.hl7.org/CodeSystem/extra-security-role-type",
                                        "code": "humanuser",
                                    },
                                    {
                                        "system": "http://hl7.org/fhir/provenance-participant-role",
                                        "code": "enterer",
                                    },
                                ],
                                "text": "User",
                            }
                        ],
                        "whoReference": {
                            "display": "SystemUser",
                            "identifier": {
                                "system": "urn:ietf:rfc:3986",
                                "value": "urn:uuid:3539c314-6e5b-4864-87c1-1195e7e2adcd",
                            },
                        },
                    },
                ],
            },
        },
    ],
}

NEMSIS_BUNDLE = {
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
                                    "code": "MR",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "IheTestPatient",
                    },
                    {
                        "system": "http://rosetta.careevolution.com/identifiers/Proprietary/1.3.6.1.4.1.37608",
                        "value": "IheTestPatient",
                    },
                ],
                "name": [{"use": "official", "family": "Smith", "given": ["Patient"]}],
                "telecom": [
                    {"system": "phone", "value": "534-555-6666", "use": "home"}
                ],
                "gender": "female",
                "birthDate": "1956-08-13",
                "deceasedBoolean": False,
                "address": [
                    {
                        "use": "home",
                        "line": ["34 Drury Lane"],
                        "city": "Disney Land",
                        "state": "CA",
                        "postalCode": "90210",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/AllergyIntolerance/7e586cfb-0c3c-43ae-ac94-acfb26b28c91",
            "resource": {
                "resourceType": "AllergyIntolerance",
                "id": "7e586cfb-0c3c-43ae-ac94-acfb26b28c91",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "clinicalStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical",
                            "code": "active",
                        },
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary/AllergyClinicalStatus",
                            "code": "active",
                            "display": "active",
                            "userSelected": True,
                        },
                    ]
                },
                "category": ["environment"],
                "criticality": "high",
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "372687004",
                            "display": "Amoxicillin",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "372687004",
                            "display": "Amoxicillin (substance)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4156860",
                            "display": "Amoxicillin",
                            "userSelected": False,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "723",
                            "display": "amoxicillin",
                            "userSelected": False,
                        },
                    ]
                },
                "patient": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "onsetDateTime": "2008-03-10T00:00:00-04:00",
                "recordedDate": "2008-03-10T00:00:00-04:00",
                "reaction": [
                    {
                        "manifestation": [
                            {
                                "coding": [
                                    {
                                        "system": "http://rosetta.careevolution.com/codes/Proprietary.CareEvolution/AllergyReaction",
                                        "code": "Rash",
                                        "display": "Rash",
                                        "userSelected": True,
                                    }
                                ]
                            }
                        ],
                        "description": "Rash",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Condition/5.4a6057fb70a64ca291b38ef98c5a7382",
            "resource": {
                "resourceType": "Condition",
                "id": "5.4a6057fb70a64ca291b38ef98c5a7382",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "clinicalStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                            "code": "active",
                        },
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary/DiagnosisStatus",
                            "code": "active",
                            "display": "active",
                            "userSelected": True,
                        },
                    ]
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                            "code": "unconfirmed",
                        }
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "urn:oid:2.16.840.1.113883.6.96",
                                "code": "55607006",
                                "display": "Problem",
                                "userSelected": True,
                            },
                            {
                                "system": "http://snomed.info/sct",
                                "code": "55607006",
                                "display": "Problem (finding)",
                                "userSelected": False,
                            },
                            {
                                "system": "https://athena.ohdsi.org/",
                                "code": "4206460",
                                "display": "Problem",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.103",
                            "code": "0261",
                            "display": "Streptobacillary fever",
                            "userSelected": True,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-9-cm/diagnosis",
                            "code": "026.1",
                            "display": "Streptobacillary fever",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "44833220",
                            "display": "Streptobacillary fever",
                            "userSelected": False,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "52138004",
                            "display": "Streptobacillary fever (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "A25.1",
                            "display": "Streptobacillosis",
                            "userSelected": False,
                        },
                    ],
                    "text": "Streptobacillary fever",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "onsetDateTime": "2009-06-07T18:00:00-04:00",
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Condition/5.41e24cc8e2e44dadaa5c1b2b6d746dad",
            "resource": {
                "resourceType": "Condition",
                "id": "5.41e24cc8e2e44dadaa5c1b2b6d746dad",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "verificationStatus": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                            "code": "unconfirmed",
                        }
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/condition-category",
                                "code": "encounter-diagnosis",
                            },
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary/DiagnosisType",
                                "code": "EncounterReason",
                                "display": "Encounter Reason",
                                "userSelected": True,
                            },
                        ]
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.103",
                            "code": "0261",
                            "display": "Streptobacillary fever",
                            "userSelected": True,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-9-cm/diagnosis",
                            "code": "026.1",
                            "display": "Streptobacillary fever",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "44833220",
                            "display": "Streptobacillary fever",
                            "userSelected": False,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "52138004",
                            "display": "Streptobacillary fever (disorder)",
                            "userSelected": False,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-10-cm",
                            "code": "A25.1",
                            "display": "Streptobacillosis",
                            "userSelected": False,
                        },
                    ],
                    "text": "Streptobacillary fever",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "encounter": {
                    "reference": "Encounter/1bdc26a5-324a-4190-a403-b63067da1c19"
                },
                "onsetDateTime": "2009-06-07T18:00:00-04:00",
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/DiagnosticReport/4.708468efc4924839b3cddb3ab5775c1f",
            "resource": {
                "resourceType": "DiagnosticReport",
                "id": "4.708468efc4924839b3cddb3ab5775c1f",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [{"use": "usual", "value": "16631200720090609061700"}],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                                "code": "LAB",
                            }
                        ],
                        "text": "LAB",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "166312007",
                            "display": "CHEM24S",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "166312007",
                            "display": "Blood chemistry (procedure)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4014134",
                            "display": "Blood chemistry",
                            "userSelected": False,
                        },
                    ],
                    "text": "CHEM24S",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-09T18:17:00-04:00",
                "issued": "2009-06-09T18:17:00-04:00",
                "result": [
                    {"reference": "Observation/2.898b46638a8a4f0f8ad5faeca51f381b"}
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/DiagnosticReport/4.9a8ce5a0c44d4affb569cf64ed82dbb2",
            "resource": {
                "resourceType": "DiagnosticReport",
                "id": "4.9a8ce5a0c44d4affb569cf64ed82dbb2",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [{"use": "usual", "value": "2660400720090608120900"}],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                                "code": "LAB",
                            }
                        ],
                        "text": "LAB",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "26604007",
                            "display": "CBC",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "26604007",
                            "display": "Complete blood count (procedure)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4132152",
                            "display": "Complete blood count",
                            "userSelected": False,
                        },
                    ],
                    "text": "CBC",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "result": [
                    {"reference": "Observation/2.82f0c47ab5274b738bd8bcd178595ed1"},
                    {"reference": "Observation/2.862f583179e347038c75895ceac08750"},
                    {"reference": "Observation/2.3a6b507900634284a6c8edf7a974e65d"},
                    {"reference": "Observation/2.48172d29edee4125ac8f975e7c6f9cf8"},
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/DiagnosticReport/4.19f34e64dac6462fa2e86113eacd32c8",
            "resource": {
                "resourceType": "DiagnosticReport",
                "id": "4.19f34e64dac6462fa2e86113eacd32c8",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [{"use": "usual", "value": "Operative20090607050000"}],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                                "code": "LAB",
                            }
                        ],
                        "text": "LAB",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/LabService",
                            "code": "Operative",
                            "display": "Operative",
                            "userSelected": True,
                        }
                    ],
                    "text": "Operative",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-07T17:00:00-04:00",
                "issued": "2009-06-07T17:00:00-04:00",
                "result": [
                    {"reference": "Observation/2.a346355cd2524a6686aeecd35e7f4aab"}
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/DiagnosticReport/4.822796b740bb446791ef4e77d0756f42",
            "resource": {
                "resourceType": "DiagnosticReport",
                "id": "4.822796b740bb446791ef4e77d0756f42",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [{"use": "usual", "value": "7930100820090608120900"}],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0074",
                                "code": "LAB",
                            }
                        ],
                        "text": "LAB",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "79301008",
                            "display": "Electrolytes measurement (procedure)",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "79301008",
                            "display": "Electrolytes measurement (procedure)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4193783",
                            "display": "Electrolytes measurement",
                            "userSelected": False,
                        },
                    ],
                    "text": "Electrolytes measurement (procedure)",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "result": [
                    {"reference": "Observation/2.1d376f381e404f629a4b668eb4bf7d72"}
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Encounter/1bdc26a5-324a-4190-a403-b63067da1c19",
            "resource": {
                "resourceType": "Encounter",
                "id": "1bdc26a5-324a-4190-a403-b63067da1c19",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "identifier": [
                    {
                        "use": "usual",
                        "system": "http://rosetta.careevolution.com/encounteridentifiers",
                        "value": "07f8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "in-progress",
                "class": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#coding",
                            "valueCoding": {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.CareEvolution/PatientClass",
                                "code": "Inpatient",
                                "display": "Inpatient",
                                "userSelected": True,
                            },
                        },
                        {
                            "url": "http://careevolution.com/fhirextensions#coding",
                            "valueCoding": {
                                "system": "https://athena.ohdsi.org/",
                                "code": "9201",
                                "display": "Inpatient Visit",
                                "userSelected": False,
                            },
                        },
                    ],
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                    "code": "IMP",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "participant": [
                    {
                        "extension": [
                            {
                                "url": "http://careevolution.com/fhirextensions#dataSource",
                                "extension": [
                                    {
                                        "url": "code",
                                        "valueString": "cj51SkDNLEqvzVeIR5m1jQ==",
                                    },
                                    {
                                        "url": "name",
                                        "valueString": "Custodian: Community Health Information Exchange;Author: Community Health Information Exchange;",
                                    },
                                ],
                            }
                        ],
                        "type": [
                            {
                                "coding": [
                                    {
                                        "system": "http://careevolution.com/fhircodes#CaregiverRelationshipType",
                                        "code": "ScheduledCaregiver",
                                        "display": "Scheduled Caregiver",
                                        "userSelected": True,
                                    }
                                ]
                            }
                        ],
                        "period": {"start": "2004-05-06T00:00:00-04:00"},
                        "individual": {
                            "reference": "Practitioner/a0ba6517-af46-44e6-8359-d7297d27a763"
                        },
                    }
                ],
                "period": {"start": "2009-06-07T17:00:00-04:00"},
                "diagnosis": [
                    {
                        "condition": {
                            "reference": "Condition/5.41e24cc8e2e44dadaa5c1b2b6d746dad"
                        },
                        "use": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                                    "code": "CC",
                                },
                                {
                                    "system": "http://rosetta.careevolution.com/codes/Proprietary/DiagnosisType",
                                    "code": "EncounterReason",
                                    "display": "Encounter Reason",
                                    "userSelected": True,
                                },
                            ]
                        },
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Encounter/3cc0c5b3-5e61-4c2d-b2f5-6d3a77b438d2",
            "resource": {
                "resourceType": "Encounter",
                "id": "3cc0c5b3-5e61-4c2d-b2f5-6d3a77b438d2",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "identifier": [
                    {
                        "use": "usual",
                        "system": "http://rosetta.careevolution.com/encounteridentifiers",
                        "value": "08f8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "in-progress",
                "class": {
                    "extension": [
                        {
                            "url": "http://careevolution.com/fhirextensions#coding",
                            "valueCoding": {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.CareEvolution/PatientClass",
                                "code": "PCPVisit",
                                "display": "PCP Visit",
                                "userSelected": True,
                            },
                        },
                        {
                            "url": "http://careevolution.com/fhirextensions#coding",
                            "valueCoding": {
                                "system": "https://athena.ohdsi.org/",
                                "code": "9202",
                                "display": "Outpatient Visit",
                                "userSelected": False,
                            },
                        },
                    ],
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                    "code": "AMB",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "period": {"start": "2009-08-10T22:00:00-04:00"},
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Practitioner/a0ba6517-af46-44e6-8359-d7297d27a763",
            "resource": {
                "resourceType": "Practitioner",
                "id": "a0ba6517-af46-44e6-8359-d7297d27a763",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner|3.1.1",
                        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-Practitioner|2.0",
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_CareEvolution",
                },
                "identifier": [
                    {
                        "use": "usual",
                        "system": "http://rosetta.careevolution.com/identifiers/CareEvolution/CaregiverIdentifier/1.3.6.1.4.1.37608_CareEvolution",
                        "value": "7v1bjE+iv1TpK7xwyhaXbw==",
                    },
                    {
                        "system": "http://rosetta.careevolution.com/identifiers/Proprietary/1.3.6.1.4.1.37608",
                        "value": "c68394cb-57ad-e411-8260-0050b664cec5",
                    },
                ],
                "name": [
                    {
                        "use": "official",
                        "family": "Smith",
                        "given": ["David", "K"],
                        "suffix": ["MD"],
                    }
                ],
                "telecom": [
                    {"system": "phone", "value": "212-555-7351", "use": "home"}
                ],
                "address": [
                    {
                        "use": "home",
                        "line": ["543 Doctor Avenue"],
                        "city": "New York",
                        "state": "NY",
                        "postalCode": "10001",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationAdministration/d07d711c-d897-410a-a3da-d605e5ed1a58",
            "resource": {
                "resourceType": "MedicationAdministration",
                "id": "d07d711c-d897-410a-a3da-d605e5ed1a58",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#medicationAdministration-scheduledTime",
                        "valueDateTime": "2009-08-11T22:00:00-04:00",
                    }
                ],
                "identifier": [
                    {"use": "usual", "value": "1cf8cd8b-58ad-e411-8260-0050b664cec5"}
                ],
                "status": "completed",
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.88",
                            "code": "C0981193",
                            "display": "Acetaminophen 325 mg oral tablet",
                            "userSelected": True,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "313782",
                            "display": "acetaminophen 325 MG Oral Tablet",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "1127433",
                            "display": "acetaminophen 325 MG Oral Tablet",
                            "userSelected": False,
                        },
                    ],
                    "text": "Acetaminophen 325 mg oral tablet",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectivePeriod": {
                    "start": "2009-08-11T22:00:00-04:00",
                    "end": "2009-08-11T22:00:00-04:00",
                },
                "request": {
                    "reference": "MedicationRequest/7f7348c8-7377-41ba-9628-5a68aa34ceec"
                },
                "dosage": {
                    "dose": {
                        "value": -1,
                        "unit": "milligram",
                        "system": "http://unitsofmeasure.org",
                        "code": "mg",
                    }
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationAdministration/b5def510-50f4-4efc-988c-a7e6e74ef61c",
            "resource": {
                "resourceType": "MedicationAdministration",
                "id": "b5def510-50f4-4efc-988c-a7e6e74ef61c",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#medicationAdministration-scheduledTime",
                        "valueDateTime": "2009-08-11T17:00:00-04:00",
                    }
                ],
                "identifier": [
                    {"use": "usual", "value": "1df8cd8b-58ad-e411-8260-0050b664cec5"}
                ],
                "status": "completed",
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.88",
                            "code": "C0973886",
                            "display": "Albuterol 0.09mg/actuat inhalant solution",
                            "userSelected": True,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "329498",
                            "display": "albuterol 0.09 MG/ACTUAT",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "1154459",
                            "display": "albuterol 0.09 MG/ACTUAT",
                            "userSelected": False,
                        },
                    ],
                    "text": "Albuterol 0.09mg/actuat inhalant solution",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectivePeriod": {
                    "start": "2009-08-11T17:00:00-04:00",
                    "end": "2009-08-11T17:00:00-04:00",
                },
                "request": {
                    "reference": "MedicationRequest/90a1faa3-43f8-4565-b170-cc4025cab2db"
                },
                "dosage": {
                    "route": {
                        "coding": [
                            {
                                "system": "urn:oid:2.16.840.1.113883.5.112",
                                "code": "PO",
                                "display": "PO",
                                "userSelected": True,
                            }
                        ]
                    },
                    "dose": {
                        "value": -1,
                        "unit": "milligram",
                        "system": "http://unitsofmeasure.org",
                        "code": "mg",
                    },
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationAdministration/e33653e5-387a-498e-acde-14cce4ddac78",
            "resource": {
                "resourceType": "MedicationAdministration",
                "id": "e33653e5-387a-498e-acde-14cce4ddac78",
                "meta": {
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608"
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#medicationAdministration-scheduledTime",
                        "valueDateTime": "2009-08-12T17:00:00-04:00",
                    }
                ],
                "identifier": [
                    {"use": "usual", "value": "1ef8cd8b-58ad-e411-8260-0050b664cec5"}
                ],
                "status": "completed",
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary.CareEvolution/MedicationProfileMedication",
                            "code": "C3243",
                            "display": "Saline",
                            "userSelected": True,
                        }
                    ],
                    "text": "Saline",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectivePeriod": {
                    "start": "2009-08-12T17:00:00-04:00",
                    "end": "2009-08-12T17:00:00-04:00",
                },
                "request": {
                    "reference": "MedicationRequest/1d1e84cd-5b15-4123-b21a-3125ef6ad192"
                },
                "dosage": {
                    "route": {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.2.16.840.1.113883.3.26.1.1/MedicationAdministrationRoute",
                                "code": "C38216",
                                "display": "Respiratory (Inhalation)",
                                "userSelected": True,
                            }
                        ]
                    },
                    "dose": {
                        "value": -1,
                        "unit": "milliliter",
                        "system": "http://unitsofmeasure.org",
                        "code": "mL",
                    },
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationRequest/90a1faa3-43f8-4565-b170-cc4025cab2db",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": "90a1faa3-43f8-4565-b170-cc4025cab2db",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PLAC",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "1df8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "completed",
                "intent": "order",
                "reportedBoolean": False,
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.88",
                            "code": "C0973886",
                            "display": "Albuterol 0.09mg/actuat inhalant solution",
                            "userSelected": True,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "329498",
                            "display": "albuterol 0.09 MG/ACTUAT",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "1154459",
                            "display": "albuterol 0.09 MG/ACTUAT",
                            "userSelected": False,
                        },
                    ],
                    "text": "Albuterol 0.09mg/actuat inhalant solution",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "authoredOn": "2009-08-11T17:00:00-04:00",
                "requester": {
                    "reference": "Practitioner/a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd"
                },
                "dosageInstruction": [
                    {
                        "text": "Albuterol 0.09mg/actuat inhalant solution",
                        "timing": {
                            "event": ["2009-08-11T17:00:00-04:00"],
                            "code": {
                                "coding": [
                                    {
                                        "system": "http://rosetta.careevolution.com/codes/Proprietary/OrderFrequency",
                                        "code": "Unspecified",
                                        "display": "Unspecified",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                        "asNeededBoolean": False,
                        "route": {
                            "coding": [
                                {
                                    "system": "urn:oid:2.16.840.1.113883.5.112",
                                    "code": "PO",
                                    "display": "PO",
                                    "userSelected": True,
                                }
                            ]
                        },
                        "doseAndRate": [
                            {
                                "doseRange": {
                                    "low": {
                                        "value": 5.5,
                                        "unit": "milligram",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "mg",
                                    },
                                    "high": {
                                        "value": 5.5,
                                        "unit": "milligram",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "mg",
                                    },
                                }
                            }
                        ],
                    }
                ],
                "dispenseRequest": {
                    "validityPeriod": {
                        "start": "2009-08-11T17:00:00-04:00",
                        "end": "2009-08-11T17:00:00-04:00",
                    }
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationRequest/72c3742d-ec08-489f-906a-bd039a8c0d07",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": "72c3742d-ec08-489f-906a-bd039a8c0d07",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PLAC",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "2ef8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "completed",
                "intent": "order",
                "reportedBoolean": False,
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.88",
                            "code": "197454",
                            "display": "Cephalexin 500 MG oral tablet",
                            "userSelected": True,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "197454",
                            "display": "cephalexin 500 MG Oral Tablet",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "1786652",
                            "display": "cephalexin 500 MG Oral Tablet",
                            "userSelected": False,
                        },
                    ],
                    "text": "Cephalexin 500 MG oral tablet",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "authoredOn": "2009-06-10T16:00:00-04:00",
                "requester": {
                    "reference": "Practitioner/a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd"
                },
                "dosageInstruction": [
                    {
                        "text": "Cephalexin 500 MG oral tablet",
                        "timing": {
                            "event": ["2009-06-10T16:00:00-04:00"],
                            "code": {
                                "coding": [
                                    {
                                        "system": "http://rosetta.careevolution.com/codes/Proprietary/OrderFrequency",
                                        "code": "Unspecified",
                                        "display": "Unspecified",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                        "asNeededBoolean": False,
                    }
                ],
                "dispenseRequest": {
                    "validityPeriod": {"start": "2009-06-10T16:00:00-04:00"}
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationRequest/44ad877e-e2de-45bd-8981-b13b3de29458",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": "44ad877e-e2de-45bd-8981-b13b3de29458",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PLAC",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "2df8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "completed",
                "intent": "order",
                "reportedBoolean": False,
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.88",
                            "code": "309362",
                            "display": "Clopidogrel 75 MG oral tablet",
                            "userSelected": True,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "309362",
                            "display": "clopidogrel 75 MG Oral Tablet",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "19075601",
                            "display": "clopidogrel 75 MG Oral Tablet",
                            "userSelected": False,
                        },
                    ],
                    "text": "Clopidogrel 75 MG oral tablet",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "authoredOn": "2009-08-15T09:00:00-04:00",
                "requester": {
                    "reference": "Practitioner/a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd"
                },
                "dosageInstruction": [
                    {
                        "text": "Clopidogrel 75 MG oral tablet",
                        "timing": {
                            "event": ["2009-08-15T09:00:00-04:00"],
                            "code": {
                                "coding": [
                                    {
                                        "system": "http://rosetta.careevolution.com/codes/Proprietary/OrderFrequency",
                                        "code": "Unspecified",
                                        "display": "Unspecified",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                        "asNeededBoolean": False,
                    }
                ],
                "dispenseRequest": {
                    "validityPeriod": {"start": "2009-08-15T09:00:00-04:00"}
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationRequest/7f7348c8-7377-41ba-9628-5a68aa34ceec",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": "7f7348c8-7377-41ba-9628-5a68aa34ceec",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PLAC",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "1cf8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "completed",
                "intent": "order",
                "reportedBoolean": False,
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.88",
                            "code": "C0981193",
                            "display": "Acetaminophen 325 mg oral tablet",
                            "userSelected": True,
                        },
                        {
                            "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                            "code": "313782",
                            "display": "acetaminophen 325 MG Oral Tablet",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "1127433",
                            "display": "acetaminophen 325 MG Oral Tablet",
                            "userSelected": False,
                        },
                    ],
                    "text": "Acetaminophen 325 mg oral tablet",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "authoredOn": "2009-08-11T22:00:00-04:00",
                "requester": {
                    "reference": "Practitioner/a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd"
                },
                "dosageInstruction": [
                    {
                        "text": "Acetaminophen 325 mg oral tablet",
                        "timing": {
                            "event": ["2009-08-11T22:00:00-04:00"],
                            "code": {
                                "coding": [
                                    {
                                        "system": "http://rosetta.careevolution.com/codes/Proprietary/OrderFrequency",
                                        "code": "Unspecified",
                                        "display": "Unspecified",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                        "asNeededBoolean": False,
                        "doseAndRate": [
                            {
                                "doseRange": {
                                    "low": {
                                        "value": 325,
                                        "unit": "milligram",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "mg",
                                    },
                                    "high": {
                                        "value": 325,
                                        "unit": "milligram",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "mg",
                                    },
                                }
                            }
                        ],
                    }
                ],
                "dispenseRequest": {
                    "validityPeriod": {
                        "start": "2009-08-11T22:00:00-04:00",
                        "end": "2009-08-11T22:00:00-04:00",
                    }
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/MedicationRequest/1d1e84cd-5b15-4123-b21a-3125ef6ad192",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": "1d1e84cd-5b15-4123-b21a-3125ef6ad192",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PLAC",
                                }
                            ]
                        },
                        "system": "urn:oid:1.3.6.1.4.1.37608",
                        "value": "1ef8cd8b-58ad-e411-8260-0050b664cec5",
                    }
                ],
                "status": "completed",
                "intent": "order",
                "reportedBoolean": False,
                "medicationCodeableConcept": {
                    "coding": [
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary.CareEvolution/OrderableItem",
                            "code": "C3243",
                            "display": "Saline",
                            "userSelected": True,
                        }
                    ],
                    "text": "Saline",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "authoredOn": "2009-08-12T17:00:00-04:00",
                "requester": {
                    "reference": "Practitioner/a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd"
                },
                "dosageInstruction": [
                    {
                        "text": "Saline",
                        "timing": {
                            "event": ["2009-08-12T17:00:00-04:00"],
                            "code": {
                                "coding": [
                                    {
                                        "system": "http://rosetta.careevolution.com/codes/Proprietary/OrderFrequency",
                                        "code": "Unspecified",
                                        "display": "Unspecified",
                                        "userSelected": True,
                                    }
                                ]
                            },
                        },
                        "asNeededBoolean": False,
                        "route": {
                            "coding": [
                                {
                                    "system": "http://rosetta.careevolution.com/codes/Proprietary.2.16.840.1.113883.3.26.1.1/OrderRoute",
                                    "code": "C38216",
                                    "display": "Respiratory (Inhalation)",
                                    "userSelected": True,
                                }
                            ]
                        },
                        "doseAndRate": [
                            {
                                "doseRange": {
                                    "low": {
                                        "value": 0.5,
                                        "unit": "milliliter",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "mL",
                                    },
                                    "high": {
                                        "value": 0.5,
                                        "unit": "milliliter",
                                        "system": "http://unitsofmeasure.org",
                                        "code": "mL",
                                    },
                                }
                            }
                        ],
                    }
                ],
                "dispenseRequest": {
                    "validityPeriod": {
                        "start": "2009-08-12T17:00:00-04:00",
                        "end": "2009-08-12T17:00:00-04:00",
                    }
                },
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Practitioner/a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd",
            "resource": {
                "resourceType": "Practitioner",
                "id": "a75b0d51-7464-4e9a-9c6c-d3a7488fd2bd",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner|3.1.1",
                        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-Practitioner|2.0",
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_CareEvolution",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#practitioner-role",
                        "valueCodeableConcept": {
                            "coding": [
                                {
                                    "system": "http://rosetta.careevolution.com/codes/Proprietary/CaregiverType",
                                    "code": "Prescriber",
                                    "display": "Prescriber",
                                    "userSelected": True,
                                }
                            ]
                        },
                    }
                ],
                "identifier": [
                    {
                        "use": "usual",
                        "system": "http://rosetta.careevolution.com/identifiers/CareEvolution/CaregiverIdentifier/1.3.6.1.4.1.37608_CareEvolution",
                        "value": "Unknown",
                    }
                ],
                "name": [{"use": "official", "family": "Unknown"}],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.898b46638a8a4f0f8ad5faeca51f381b",
            "resource": {
                "resourceType": "Observation",
                "id": "2.898b46638a8a4f0f8ad5faeca51f381b",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.708468efc4924839b3cddb3ab5775c1f"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "275790008",
                            "display": "CHLORIDE",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "275790008",
                            "display": "Chloride in sample (finding)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4077512",
                            "display": "Chloride in sample",
                            "userSelected": False,
                        },
                    ],
                    "text": "CHLORIDE",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-09T18:17:00-04:00",
                "issued": "2009-06-09T18:17:00-04:00",
                "valueString": "112 MMOL/L",
                "interpretation": [
                    {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/Acuity",
                                "code": "H",
                                "display": "H",
                                "userSelected": True,
                            },
                            {
                                "system": "http://hl7.org/fhir/v3/ObservationInterpretation",
                                "code": "H",
                                "display": "High",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "referenceRange": [
                    {
                        "low": {"value": 98, "unit": "MMOL/L"},
                        "high": {"value": 107, "unit": "MMOL/L"},
                        "text": "98-107 MMOL/L",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.3a6b507900634284a6c8edf7a974e65d",
            "resource": {
                "resourceType": "Observation",
                "id": "2.3a6b507900634284a6c8edf7a974e65d",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.9a8ce5a0c44d4affb569cf64ed82dbb2"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "16378004",
                            "display": "PLT",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "16378004",
                            "display": "Platelet (cell structure)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4039428",
                            "display": "Platelet",
                            "userSelected": False,
                        },
                    ],
                    "text": "PLT",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "valueString": "132 K/CUMM",
                "interpretation": [
                    {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/Acuity",
                                "code": "L",
                                "display": "L",
                                "userSelected": True,
                            },
                            {
                                "system": "http://hl7.org/fhir/v3/ObservationInterpretation",
                                "code": "L",
                                "display": "Low",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "referenceRange": [
                    {
                        "low": {"value": 150, "unit": "K/CUMM"},
                        "high": {"value": 450, "unit": "K/CUMM"},
                        "text": "150-450 K/CUMM",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.a346355cd2524a6686aeecd35e7f4aab",
            "resource": {
                "resourceType": "Observation",
                "id": "2.a346355cd2524a6686aeecd35e7f4aab",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.19f34e64dac6462fa2e86113eacd32c8"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/LabObservationType",
                            "code": "Operative",
                            "display": "Operative",
                            "userSelected": True,
                        }
                    ],
                    "text": "OPERATIVE NOTE\nDICTATED BY: Jack Blue, MD\nDICTATED: 6/7/2009  8:03 P   000087489\nTRANSCRIBED:  6/8/2009  1:06 A  vl  D\nPATIENT NAME: Test, Ihe\nHEALTH RECORD NO.: 123456783\nBILLING NO.: 88888888\nROOM N",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-07T17:00:00-04:00",
                "issued": "2009-06-07T17:00:00-04:00",
                "valueString": "OPERATIVE NOTE\nDICTATED BY: Jack Blue, MD\nDICTATED: 6/7/2009  8:03 P   000087489\nTRANSCRIBED:  6/8/2009  1:06 A  vl  D\nPATIENT NAME: Test, Ihe\nHEALTH RECORD NO.: 123456783\nBILLING NO.: 88888888\nROOM NO.: SIC\nDate of Procedure: 11/28/06\nPREOPERATIVE DIAGNOSES: Aortic stenosis and mitral\ninsufficiency.\nPOSTOPERATIVE DIAGNOSES: Aortic stenosis and mitral\ninsufficiency.\nPROCEDURE PERFORMED: Aortic valve replacement with a 21 mm\nEdwards Magna bovine pericardial bioprosthesis and a reverse\nsaphenous vein graft to the right coronary.\nSURGEON: Dr. Blue.\nASSISTANT: Pat Yellow, CST.\nANESTHESIA: General tracheal anesthesia, Dr. Green.\nAortic cross clamp time was 117 minutes.\nCardiopulmonary bypass time was 168 minutes.\nAtrial and ventricular pacing wires.\nDrains - 32 French mediastinal chest tube, 28 French\nmediastinal chest tube.\nFINDINGS: Good saphenous vein conduit, normal ascending aorta,\naortic valve was trileaflet with heavy calcification to the\nleaflets. The annulus was not too heavily calcified with\nmoderate aortic annular calcification.  Also noted was a right\ncoronary ostial intimal flap that was noted after I was\ngetting ready to seat the valve and this will be described in\nthe text of the operation; therefore the right coronary was\ngrafted.  The right coronary was a 2.5 mm vessel with no\ndistal disease.\nINDICATIONS FOR PROCEDURE:  The patient is a 73-year-old woman\nwho was found to have known aortic stenosis and found to have\nbreast carcinoma needing resection of her breast cancer;\nhowever, has had severe aortic stenosis prior to undergoing\nbreast cancer surgery.  She needed her heart fixed.  The\npatient is brought to the operating room for aortic valve\nreplacement.  Preoperative echocardiogram demonstrates severe\naortic stenosis and moderate aortic insufficiency and 2+\nmitral insufficiency.  Intraoperative transesophageal\nechocardiogram was performed by Dr. Mauve.\nDESCRIPTION OF THE PROCEDURE: The patient was brought to the\noperating room and placed in a comfortable supine position on\nthe operating table.  She underwent induction of general\nendotracheal anesthesia and placement of invasive monitor,\nlines and intraoperative echocardiogram by Dr. Mauve.\nEchocardiogram demonstrated severe aortic stenosis and heavily\ncalcified leaflets with moderate mitral insufficiency given\nher age.  It was my impression that decompressing her outflow\ntract would improve her mitral valve insufficiency.  The\npatient was then positioned, prepped and draped in the usual\nsterile fashion.  A median sternotomy was accomplished.  The\nchest was opened and a mediastinal dissection proceeded. The\npericardium was opened and suspended. The patient was\nheparinized.  The distal ascending aorta was cannulated\nthrough double aortic pursestring sutures.  A two stage venous\ncannula was positioned to the right atrial appendage\npursestring and the patient was initiated on cardiopulmonary\nbypass.  Antegrade and retrograde cardioplegia cannulas were\npositioned.  An LV sump cannula was positioned through right\nsuperior pulmonary vein.  The patient was cooled to 32 degrees\ncentigrade. The aorta was cross clamped and antegrade and\nretrograde cold blood cardioplegia was administered.  After\ndiastolic rest of the heart we made a transverse aortotomy\nwith a hockey stick extension down into the noncoronary sinus.\nExposure of the valve was actually pretty descent. Valve\nfindings as noted previously. The valve was sharply excised.\nThe majority of the annular debridement was done fortunately\nwith the scissors; i.e., the majority of the annular\ncalcifications were in the leaflets and not so much in the\nannulus.  Once we got the leaflets cut out the annulus was d\nbrided of the remainder of the calcific debris. I incised it\nprior to placement of sutures and it sized out to 21 mm sized\nout very easily and in fact a 23 almost fit. I then placed\nmultiple annular sutures circumferentially about the annulus\nthat was consistent with interrupted 2-0 Ethibond horizontal\nmattress pledgeted sutures with pledgets on the ventricular\nside.  Once we got all our sutures in, I resized the 21 mm\nsizer.  A 21 interannular sizer was quit snug; however, the\nsizer on the supra-annular position looked quite comfortable.\nA 21 mm valve was brought up to the field and it was washed\nand then brought to operative field.  While I was examining\nthe root of the heart I noted that there an intimal dissection\nof the ostium of the right coronary that is completely\nunexplainable. There was no direct cannulation of the right\ncoronary ostium.  There was no mechanical debridement at the\nright coronary ostium but fortuitously identified the right\ncoronary intimal tear and it was an intimal tear of the aortic\nwall and it extended to the right coronary ostium.  I tacked\nthis intima down to the aortic wall with interrupted\nhorizontal mattress 5-0 Prolene suture but I was very\nuncomfortable just simply leaving this in place that it posed\nthe possibility for acute right coronary dissection, RV\ninfarct, and inferior wall infarct postoperatively. Therefore,\neven though she did not have any coronary disease, I was very\nconcerned about leaving her with an unprotected right\ncoronary.  I therefore asked Pat Yellow, my assistant,\nto scrub and take a segment of vein from the left lower leg\ngreater saphenous vein was harvested and the wound was closed\nin layers with absorbable suture.  While she was taking vein,\nI placed annular sutures through the valve, sewing ring the\nvalve and then seated down into the annulus and it seated\nnicely.  It was seated first in the left coronary sinus\nfollowed by the right coronary sinus followed by the\nnoncoronary sinus.  The remainder of the sutures was tied\ncircumferentially.  I examined the valve and it appeared to be\nseated well and I was very pleased with the seating.\nPat Yellow was still procuring vein when I was closing\nthe aortotomy.  The aortotomy was closed in a two layer\nfashion with running 4-0 Prolene in a two layer fashion.  The\nfirst layer was a running horizontal mattress with 4-0 Prolene\nfollowed by over and over 4-0 Prolene.  By this time the vein\nwas out.  I identified a spot in the mid right coronary about\nthe level of the acute margin, made an arteriotomy and sewed\nthe vein graft end-to-side with running 7-0 Prolene suture.  I\nmade a single 4.4 mm aortotomy distal to my transverse\naortotomy and anastomosed the vein graft end-to-side with\nrunning 5-0 Prolene suture.  The patient was rewarmed while I\nreconstructed the last anastomosis and a warm dose of\ncardioplegia was given through the retrograde cannula.  The\npatient was positioned in Trendelenburg position. The\nventricle and aorta were de-aired out the ascending aorta.\nThe patient was positioned head down position.  The aortic\ncross clamp was removed.  The patient's rhythm returned to\nventricular fibrillation.  I defibrillated the heart several\ntimes with loading dose of Lidocaine and amiodarone and was\nfinally able to get her defibrillated to a paced rhythm.  The\ngraft was de-aired and the bulldog was released.  The\naortotomy was hemostatic. Atrial and ventricular pacing wires\nwere positioned and mediastinal drains were positioned and\nproximal graft markers were positioned.  With satisfactory\nreperfusion time, we went ahead and ventilated the patient,\nremoved the retrograde cannula was previously removed.  The LV\nsump cannula was removed once I had the heart beating.  We\nthen proceeded with echocardiogram interrogation.\nEchocardiogram interrogation demonstrated satisfactory\nde-airing and satisfactory valve function with no aortic\ninsufficiency and only trivial mitral insufficiency.  With\nthat result, we removed the antegrade cardioplegia needle and\nthen weaned and separated from cardiopulmonary bypass on low\ndose inotropic support.  The venous cannula was removed. The\npump line was administered through the aortic cannula with\nsatisfactory hemodynamics.  Protamine was administered.  We\ngained hemostasis through the mediastinum.  The aorta was\nde-cannulated.  Pursestring sutures were secured. With\nsatisfactory hemostasis we preceded closure.  The sternum was\napproximated with interrupted #7 stainless steel wires.  The\ndeep fascia was closed with running #1 PDS.  The subcutaneous\ntissue was closed with 2-0 Vicryl. The skin edges were closed\nwith 3-0 Monocryl.  The patient's wounds were dressed in a\ndry, sterile dressing.  The patient tolerated the procedure\nwell with no operative complications.  The patient was\nreturned to the surgical intensive care unit in critical\ncondition.\n___________________________\nJack Blue, MD\ncc:  Donald M Red, MD\n     Jack Blue, MD\n     Chip Orange, MD\nDOCUMENT #: 2487825",
                "referenceRange": [{"text": "unknown"}],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.82f0c47ab5274b738bd8bcd178595ed1",
            "resource": {
                "resourceType": "Observation",
                "id": "2.82f0c47ab5274b738bd8bcd178595ed1",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.9a8ce5a0c44d4affb569cf64ed82dbb2"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "767002",
                            "display": "WBC",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "767002",
                            "display": "White blood cell count (procedure)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4298431",
                            "display": "White blood cell count",
                            "userSelected": False,
                        },
                    ],
                    "text": "WBC",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "valueString": "16.6 K/CUMM",
                "interpretation": [
                    {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/Acuity",
                                "code": "H",
                                "display": "H",
                                "userSelected": True,
                            },
                            {
                                "system": "http://hl7.org/fhir/v3/ObservationInterpretation",
                                "code": "H",
                                "display": "High",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "referenceRange": [
                    {
                        "low": {"value": 4, "unit": "K/CUMM"},
                        "high": {"value": 10.5, "unit": "K/CUMM"},
                        "text": "4.0-10.5 K/CUMM",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.48172d29edee4125ac8f975e7c6f9cf8",
            "resource": {
                "resourceType": "Observation",
                "id": "2.48172d29edee4125ac8f975e7c6f9cf8",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.9a8ce5a0c44d4affb569cf64ed82dbb2"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "28317006",
                            "display": "HCT",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "28317006",
                            "display": "Hematocrit determination (procedure)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4151358",
                            "display": "Hematocrit determination",
                            "userSelected": False,
                        },
                    ],
                    "text": "HCT",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "valueString": "28.6 %",
                "interpretation": [
                    {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/Acuity",
                                "code": "L",
                                "display": "L",
                                "userSelected": True,
                            },
                            {
                                "system": "http://hl7.org/fhir/v3/ObservationInterpretation",
                                "code": "L",
                                "display": "Low",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "referenceRange": [
                    {
                        "low": {
                            "value": 37,
                            "unit": "%",
                            "system": "http://unitsofmeasure.org",
                            "code": "%",
                        },
                        "high": {
                            "value": 47,
                            "unit": "%",
                            "system": "http://unitsofmeasure.org",
                            "code": "%",
                        },
                        "text": "37.0-47.0 %",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.862f583179e347038c75895ceac08750",
            "resource": {
                "resourceType": "Observation",
                "id": "2.862f583179e347038c75895ceac08750",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.9a8ce5a0c44d4affb569cf64ed82dbb2"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "38082009",
                            "display": "HGB",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "38082009",
                            "display": "Hemoglobin (substance)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4244232",
                            "display": "Hemoglobin",
                            "userSelected": False,
                        },
                    ],
                    "text": "HGB",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "valueString": "10.2 G/DL",
                "interpretation": [
                    {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/Acuity",
                                "code": "L",
                                "display": "L",
                                "userSelected": True,
                            },
                            {
                                "system": "http://hl7.org/fhir/v3/ObservationInterpretation",
                                "code": "L",
                                "display": "Low",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "referenceRange": [
                    {
                        "low": {"value": 12.5, "unit": "G/DL"},
                        "high": {"value": 16, "unit": "G/DL"},
                        "text": "12.5-16.0 G/DL",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Observation/2.1d376f381e404f629a4b668eb4bf7d72",
            "resource": {
                "resourceType": "Observation",
                "id": "2.1d376f381e404f629a4b668eb4bf7d72",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "extension": [
                    {
                        "url": "http://careevolution.com/fhirextensions#observation-reportReference",
                        "valueReference": {
                            "reference": "DiagnosticReport/4.822796b740bb446791ef4e77d0756f42"
                        },
                    }
                ],
                "status": "final",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                "code": "laboratory",
                            }
                        ],
                        "text": "laboratory",
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.96",
                            "code": "31811003",
                            "display": "CARBON DIOXIDE",
                            "userSelected": True,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "31811003",
                            "display": "Carbon dioxide (substance)",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "4135927",
                            "display": "Carbon dioxide",
                            "userSelected": False,
                        },
                    ],
                    "text": "CARBON DIOXIDE",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "effectiveDateTime": "2009-06-08T12:09:00-04:00",
                "issued": "2009-06-08T12:09:00-04:00",
                "valueString": "26 MMOL/L",
                "interpretation": [
                    {
                        "coding": [
                            {
                                "system": "http://rosetta.careevolution.com/codes/Proprietary.DemoNamespace/Acuity",
                                "code": "N",
                                "display": "N",
                                "userSelected": True,
                            },
                            {
                                "system": "http://hl7.org/fhir/v3/ObservationInterpretation",
                                "code": "N",
                                "display": "Normal",
                                "userSelected": False,
                            },
                        ]
                    }
                ],
                "referenceRange": [
                    {
                        "low": {"value": 22, "unit": "MMOL/L"},
                        "high": {"value": 31, "unit": "MMOL/L"},
                        "text": "22-31 MMOL/L",
                    }
                ],
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Procedure/7.bc640751160d4dce960769e09f6a7de1",
            "resource": {
                "resourceType": "Procedure",
                "id": "7.bc640751160d4dce960769e09f6a7de1",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "status": "completed",
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.12",
                            "code": "3227",
                            "display": "Bronchoscopic bronchial thermoplasty, ablation of airway smooth muscle",
                            "userSelected": True,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-9-cm/procedure",
                            "code": "32.27",
                            "display": "Bronchoscopic bronchial thermoplasty, ablation of airway smooth muscle",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "40756810",
                            "display": "Bronchoscopic bronchial thermoplasty, ablation of airway smooth muscle",
                            "userSelected": False,
                        },
                    ],
                    "text": "Bronchoscopic bronchial thermoplasty, ablation of airway smooth muscle",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "performedDateTime": "2009-08-10T23:00:00-04:00",
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Procedure/7.93805cca981542d7a67e487f0b94944a",
            "resource": {
                "resourceType": "Procedure",
                "id": "7.93805cca981542d7a67e487f0b94944a",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "status": "completed",
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.12",
                            "code": "0396",
                            "display": "Percutaneous denervation of facet",
                            "userSelected": True,
                        },
                        {
                            "system": "http://hl7.org/fhir/sid/icd-9-cm/procedure",
                            "code": "03.96",
                            "display": "Percutaneous denervation of facet",
                            "userSelected": False,
                        },
                        {
                            "system": "https://athena.ohdsi.org/",
                            "code": "2000195",
                            "display": "Percutaneous denervation of facet",
                            "userSelected": False,
                        },
                        {
                            "system": "http://snomed.info/sct",
                            "code": "50055008",
                            "display": "Percutaneous denervation of facet (procedure)",
                            "userSelected": False,
                        },
                    ],
                    "text": "Percutaneous denervation of facet",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "performedDateTime": "2009-06-07T20:00:00-04:00",
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Procedure/7.2ed0fe30094a46e7bf6b3ebe69ead24a",
            "resource": {
                "resourceType": "Procedure",
                "id": "7.2ed0fe30094a46e7bf6b3ebe69ead24a",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "status": "completed",
                "code": {
                    "coding": [
                        {
                            "system": "urn:oid:2.16.840.1.113883.6.103",
                            "code": "465",
                            "display": "Treatment for Upper Respiratory Infection",
                            "userSelected": True,
                        }
                    ],
                    "text": "Treatment for Upper Respiratory Infection",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "performedDateTime": "2009-07-01T12:00:00-04:00",
            },
        },
        {
            "fullUrl": "https://api.rosetta.careevolution.com/Procedure/7.14e26bb09d7649b2a6ce10f794ca8960",
            "resource": {
                "resourceType": "Procedure",
                "id": "7.14e26bb09d7649b2a6ce10f794ca8960",
                "meta": {
                    "profile": [
                        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure|3.1.1"
                    ],
                    "source": "http://rosetta.careevolution.com/identifiers/CareEvolution/MRN/1.3.6.1.4.1.37608_1.3.6.1.4.1.37608",
                },
                "status": "completed",
                "code": {
                    "coding": [
                        {
                            "system": "http://rosetta.careevolution.com/codes/Proprietary.CareEvolution/ProcedureCode",
                            "code": "OtherThymusOperations",
                            "display": "Oth thorac op thymus NOS",
                            "userSelected": True,
                        }
                    ],
                    "text": "Other and unspecified thoracoscopic operations on thymus",
                },
                "subject": {
                    "reference": "Patient/35b77437-425d-419c-90b5-af4bc433ebe9"
                },
                "performedDateTime": "2009-06-07T20:30:00-04:00",
            },
        },
        {
            "resource": {
                "resourceType": "OperationOutcome",
                "issue": [
                    {
                        "severity": "warning",
                        "code": "processing",
                        "details": {
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
                                    "code": "CdaParsingWarning",
                                }
                            ],
                            "text": "Labs: Missing description in the reference dictionary for #labgroup_3. Line Number - 662, XPath - ClinicalDocument/component/structuredBody/component/section/entry/organizer/code/originalText/reference",
                        },
                    },
                    {
                        "severity": "warning",
                        "code": "processing",
                        "details": {
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
                                    "code": "CdaParsingWarning",
                                }
                            ],
                            "text": "Labs: Missing description in the reference dictionary for #labgroup_5. Line Number - 701, XPath - ClinicalDocument/component/structuredBody/component/section/entry/organizer/code/originalText/reference",
                        },
                    },
                    {
                        "severity": "warning",
                        "code": "processing",
                        "details": {
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
                                    "code": "CdaParsingWarning",
                                }
                            ],
                            "text": "Labs: Missing description in the reference dictionary for #labgroup_10. Line Number - 821, XPath - ClinicalDocument/component/structuredBody/component/section/entry/organizer/code/originalText/reference",
                        },
                    },
                    {
                        "severity": "warning",
                        "code": "processing",
                        "details": {
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
                                    "code": "CdaParsingWarning",
                                }
                            ],
                            "text": "Labs: Missing description in the reference dictionary for #reportheader_12. Line Number - 860, XPath - ClinicalDocument/component/structuredBody/component/section/entry/organizer/code/originalText/reference",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Encounters",
                                }
                            ],
                            "text": "Encounters:\nTotal: 2\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 3,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Reports",
                                }
                            ],
                            "text": "Reports:\nTotal: 3\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 1,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Problems",
                                }
                            ],
                            "text": "Problems:\nTotal: 1\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 1,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Allergies",
                                }
                            ],
                            "text": "Allergies:\nTotal: 1\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 7,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Labs",
                                }
                            ],
                            "text": "Labs:\nTotal: 7\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 5,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Medications",
                                }
                            ],
                            "text": "Medications:\nTotal: 5\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 4,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Procedures",
                                }
                            ],
                            "text": "Procedures:\nTotal: 4\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#Total",
                                    "valueInteger": 1,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#InvalidEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#DuplicateEntries",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Section#IgnoredEntries",
                                    "valueInteger": 1,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDASectionSummary",
                                    "code": "Vitals",
                                }
                            ],
                            "text": "Vitals:\nTotal: 1\nInvalidEntries: 0\nDuplicateEntries: 0\nIgnoredEntries: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Document#UnstructuredDocument",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Document#MissingEncompassingEncounter",
                                    "valueBoolean": True,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Document#MissingLegalAuthenticator",
                                    "valueBoolean": True,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Document#MissingSignatureCode",
                                    "valueBoolean": True,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Document",
                                }
                            ],
                            "text": "Document:\nUnstructuredDocument: False\nMissingEncompassingEncounter: True\nMissingLegalAuthenticator: True\nMissingSignatureCode: True",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingGender",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingRace",
                                    "valueBoolean": True,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingEthnicity",
                                    "valueBoolean": True,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingDateOfBirth",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingPatientStreetAddress",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingPatientAddressCity",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingPatientAddressState",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingPatientAddressPostalCode",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingPatientPhoneNumber",
                                    "valueBoolean": False,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#MissingPatientEMailAddress",
                                    "valueBoolean": True,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Patient#ByIdentifierType",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "1.3.6.1.4.1.37608",
                                        "code": "1.3.6.1.4.1.37608",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Patient",
                                }
                            ],
                            "text": "Patient:\nMissingGender: False\nMissingRace: True\nMissingEthnicity: True\nMissingDateOfBirth: False\nMissingPatientStreetAddress: False\nMissingPatientAddressCity: False\nMissingPatientAddressState: False\nMissingPatientAddressPostalCode: False\nMissingPatientPhoneNumber: False\nMissingPatientEMailAddress: True\nByIdentifierType 1.3.6.1.4.1.37608: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#Total",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#MissingDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#MissingStopDate",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#MissingStopDateByStatus",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "MissingStatus",
                                        "code": "MissingStatus",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#MissingStopDateByStatus",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "active:active",
                                        "code": "active:active",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#ByType",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "EncounterReason:Encounter Reason",
                                        "code": "EncounterReason:Encounter Reason",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#ByType",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "55607006:Problem",
                                        "code": "55607006:Problem",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#ByStatus",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "MissingStatus",
                                        "code": "MissingStatus",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#ByStatus",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "active:active",
                                        "code": "active:active",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Problems#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 2,
                                        "unit": "2.16.840.1.113883.6.103",
                                        "code": "2.16.840.1.113883.6.103",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Problems",
                                }
                            ],
                            "text": "Problems:\nTotal: 2\nMissingDate: 0\nMissingStopDate: 2\nMissingStopDateByStatus MissingStatus: 1\nMissingStopDateByStatus active:active: 1\nByType EncounterReason:Encounter Reason: 1\nByType 55607006:Problem: 1\nByStatus MissingStatus: 1\nByStatus active:active: 1\nBySourceCodingSystem 2.16.840.1.113883.6.103: 2",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Procedures#Total",
                                    "valueInteger": 4,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Procedures#MissingDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Procedures#ByStatus",
                                    "valueQuantity": {
                                        "value": 4,
                                        "unit": "completed:completed",
                                        "code": "completed:completed",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Procedures#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 2,
                                        "unit": "2.16.840.1.113883.6.12",
                                        "code": "2.16.840.1.113883.6.12",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Procedures#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "2.16.840.1.113883.6.103",
                                        "code": "2.16.840.1.113883.6.103",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Procedures#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "Proprietary.CareEvolution",
                                        "code": "Proprietary.CareEvolution",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Procedures",
                                }
                            ],
                            "text": "Procedures:\nTotal: 4\nMissingDate: 0\nByStatus completed:completed: 4\nBySourceCodingSystem 2.16.840.1.113883.6.12: 2\nBySourceCodingSystem 2.16.840.1.113883.6.103: 1\nBySourceCodingSystem Proprietary.CareEvolution: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#Total",
                                    "valueInteger": 5,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#MissingOrderDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#MissingStopDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#MissingOrderingCaregiver",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#MissingCaregiver",
                                    "valueInteger": 5,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#ByStatus",
                                    "valueQuantity": {
                                        "value": 5,
                                        "unit": "completed:completed",
                                        "code": "completed:completed",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 4,
                                        "unit": "2.16.840.1.113883.6.88",
                                        "code": "2.16.840.1.113883.6.88",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Medications#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "Proprietary.CareEvolution",
                                        "code": "Proprietary.CareEvolution",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Medications",
                                }
                            ],
                            "text": "Medications:\nTotal: 5\nMissingOrderDate: 0\nMissingStopDate: 0\nMissingOrderingCaregiver: 0\nMissingCaregiver: 5\nByStatus completed:completed: 5\nBySourceCodingSystem 2.16.840.1.113883.6.88: 4\nBySourceCodingSystem Proprietary.CareEvolution: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Allergies#Total",
                                    "valueInteger": 1,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Allergies#MissingReportedDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Allergies#MissingOnsetDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Allergies#MissingReactions",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Allergies#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "2.16.840.1.113883.6.96",
                                        "code": "2.16.840.1.113883.6.96",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Allergies",
                                }
                            ],
                            "text": "Allergies:\nTotal: 1\nMissingReportedDate: 0\nMissingOnsetDate: 0\nMissingReactions: 0\nBySourceCodingSystem 2.16.840.1.113883.6.96: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabObservations#Total",
                                    "valueInteger": 7,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabObservations#MissingDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabObservations#MissingPerformer",
                                    "valueInteger": 7,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabObservations#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 6,
                                        "unit": "2.16.840.1.113883.6.96",
                                        "code": "2.16.840.1.113883.6.96",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabObservations#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "Proprietary.DemoNamespace",
                                        "code": "Proprietary.DemoNamespace",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "LabObservations",
                                }
                            ],
                            "text": "LabObservations:\nTotal: 7\nMissingDate: 0\nMissingPerformer: 7\nBySourceCodingSystem 2.16.840.1.113883.6.96: 6\nBySourceCodingSystem Proprietary.DemoNamespace: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabPanels#Total",
                                    "valueInteger": 4,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabPanels#MissingDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabPanels#WithSingleLabObservation",
                                    "valueInteger": 3,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabPanels#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 3,
                                        "unit": "2.16.840.1.113883.6.96",
                                        "code": "2.16.840.1.113883.6.96",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/LabPanels#BySourceCodingSystem",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "Proprietary.DemoNamespace",
                                        "code": "Proprietary.DemoNamespace",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "LabPanels",
                                }
                            ],
                            "text": "LabPanels:\nTotal: 4\nMissingDate: 0\nWithSingleLabObservation: 3\nBySourceCodingSystem 2.16.840.1.113883.6.96: 3\nBySourceCodingSystem Proprietary.DemoNamespace: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Encounters#Total",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Encounters#MissingAdmitDate",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Encounters#MissingPatientClass",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Encounters#MissingLocation",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Encounters#MissingCaregiversByPatientClass",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "PCPVisit:PCP Visit",
                                        "code": "PCPVisit:PCP Visit",
                                    },
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/CDAParsingSummary/Encounters#CaregiverRelationshipsByType",
                                    "valueQuantity": {
                                        "value": 1,
                                        "unit": "ScheduledCaregiver",
                                        "code": "ScheduledCaregiver",
                                    },
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAParsingSummary",
                                    "code": "Encounters",
                                }
                            ],
                            "text": "Encounters:\nTotal: 2\nMissingAdmitDate: 0\nMissingPatientClass: 0\nMissingLocation: 2\nMissingCaregiversByPatientClass PCPVisit:PCP Visit: 1\nCaregiverRelationshipsByType ScheduledCaregiver: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#Total",
                                    "valueInteger": 5,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#WellCodedCount",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#EnhancedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#ParsedCount",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#GarbageCount",
                                    "valueInteger": 1,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/RosettaCodingUplift",
                                    "code": "Medications",
                                }
                            ],
                            "text": "Medications:\nTotal: 5\nWellCodedCount: 2\nEnhancedCount: 0\nParsedCount: 2\nGarbageCount: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#Total",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#WellCodedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#EnhancedCount",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#ParsedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#GarbageCount",
                                    "valueInteger": 0,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/RosettaCodingUplift",
                                    "code": "Problems",
                                }
                            ],
                            "text": "Problems:\nTotal: 2\nWellCodedCount: 0\nEnhancedCount: 2\nParsedCount: 0\nGarbageCount: 0",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#Total",
                                    "valueInteger": 4,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#WellCodedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#EnhancedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#ParsedCount",
                                    "valueInteger": 2,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#GarbageCount",
                                    "valueInteger": 2,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/RosettaCodingUplift",
                                    "code": "Services",
                                }
                            ],
                            "text": "Services:\nTotal: 4\nWellCodedCount: 0\nEnhancedCount: 0\nParsedCount: 2\nGarbageCount: 2",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#Total",
                                    "valueInteger": 7,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#WellCodedCount",
                                    "valueInteger": 6,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#EnhancedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#ParsedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#GarbageCount",
                                    "valueInteger": 1,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/RosettaCodingUplift",
                                    "code": "Labs",
                                }
                            ],
                            "text": "Labs:\nTotal: 7\nWellCodedCount: 6\nEnhancedCount: 0\nParsedCount: 0\nGarbageCount: 1",
                        },
                    },
                    {
                        "severity": "information",
                        "code": "informational",
                        "details": {
                            "extension": [
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#Total",
                                    "valueInteger": 4,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#WellCodedCount",
                                    "valueInteger": 3,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#EnhancedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#ParsedCount",
                                    "valueInteger": 0,
                                },
                                {
                                    "url": "https://quality.rosetta.careevolution.com/v1/Extensions/RosettaUplift/Coding#GarbageCount",
                                    "valueInteger": 1,
                                },
                            ],
                            "coding": [
                                {
                                    "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/RosettaCodingUplift",
                                    "code": "Reports",
                                }
                            ],
                            "text": "Reports:\nTotal: 4\nWellCodedCount: 3\nEnhancedCount: 0\nParsedCount: 0\nGarbageCount: 1",
                        },
                    },
                ],
            },
            "search": {"mode": "outcome"},
        },
    ],
}
