export class OrchestrateError extends Error {
  constructor(message: string) {
    super(message);
    this.name = this.constructor.name;
  }
}

export class OrchestrateHttpError extends OrchestrateError {
  constructor(message: string) {
    super(message);
    this.name = this.constructor.name;
  }
}

export class OrchestrateClientError extends OrchestrateError {
  constructor(response_text: string, issues: string[]) {
    let message;
    if (issues.length > 0) {
      message = `\n  * ${issues.join(" \n  * ")}`;
    }
    else {
      message = response_text;
    }
    super(message);
    this.name = this.constructor.name;
  }
}
