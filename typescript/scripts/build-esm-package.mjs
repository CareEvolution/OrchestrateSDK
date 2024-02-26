import { writeFile } from "fs";

const content = JSON.stringify({ type: "module" });
writeFile("./dist/esm/package.json", content, (err) => {
	if (err) {
		throw err;
	}
});
