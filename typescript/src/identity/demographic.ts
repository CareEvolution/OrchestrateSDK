export type BlindedDemographic = {
  data: string;
  version: number;
};

export type Demographic = {
  firstName?: string | undefined;
  middleName?: string | undefined;
  lastName?: string | undefined;
  maidenName?: string | undefined;
  gender?: string | undefined;
  race?: string | undefined;
  homePhoneNumber?: string | undefined;
  cellPhoneNumber?: string | undefined;
  email?: string | undefined;
  dob?: string | undefined;
  street?: string | undefined;
  city?: string | undefined;
  state?: string | undefined;
  zipCode?: string | undefined;
  mrn?: string | undefined;
  hcid?: string | undefined;
  ssn?: string | undefined;
  medicaidID?: string | undefined;
};
