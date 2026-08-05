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

export class OperationOutcomeIssue {
  severity: string;
  code: string;
  diagnostics: string;
  details: string;

  constructor(severity: string, code: string, diagnostics: string, details: string) {
    this.severity = severity;
    this.code = code;
    this.diagnostics = diagnostics;
    this.details = details;
  }

  toString(): string {
    let s = `${this.severity}: ${this.code}`;
    const message = [this.details, this.diagnostics]
      .filter(msg => msg)
      .join("; ");
    if (message) {
      s += ` - ${message}`;
    }
    return s;
  }
}

export class OrchestrateClientError extends OrchestrateError {
  responseText: string;
  issues: OperationOutcomeIssue[];
  statusCode: number;

  constructor(responseText: string, issues: OperationOutcomeIssue[], statusCode: number = 0) {
    const message = issues.length > 0
      ? `\n  * ${issues.map(i => i.toString()).join(" \n  * ")}`
      : responseText;
    super(message);
    this.name = this.constructor.name;
    this.responseText = responseText;
    this.issues = issues;
    this.statusCode = statusCode;
  }
}
