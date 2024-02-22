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
