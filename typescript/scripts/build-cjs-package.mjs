import { writeFile } from "fs";

const content = JSON.stringify({ type: "commonjs" });
writeFile("./dist/cjs/package.json", content, (err) => {
	if (err) {
		throw err;
	}
});
