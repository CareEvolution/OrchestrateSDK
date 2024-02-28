import { LocalHashingApi } from "../../src/identity/localHashing.js";
import { describe, expect, it } from "vitest";
import { Demographic } from "../../src/identity/demographic.js";
import dotenv from 'dotenv';

dotenv.config({ path: "../.env" });
const localHashingApi = new LocalHashingApi();

const demographic: Demographic = {
  firstName: "John",
  lastName: "Doe",
  dob: "1980-01-01",
  gender: "male",
};

describe("LocalHashingApi hash", () => {
  it("should hash by demographic", async () => {
    const result = await localHashingApi.hash(demographic);

    expect(result.version).greaterThan(0);
    expect(result.advisories.invalidDemographicFields).toEqual([]);
  });

  it("with invalid demographic fields should return an advisory", async () => {
    const result = await localHashingApi.hash({
      ...demographic
      , dob: "121980-01-01"
    });

    expect(result.version).greaterThan(0);
    expect(result.advisories.invalidDemographicFields).toEqual(["dob"]);
  });
});

describe("LocalHashingApi constructor", () => {
  it("should build from passed url", () => {
    const localHashingApi = new LocalHashingApi({ url: "http://localhost:8080" });

    expect(localHashingApi.toString()).toContain("http://localhost:8080");
  });
});