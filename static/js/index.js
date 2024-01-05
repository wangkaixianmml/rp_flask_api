// static/js/index.js

import { Notes } from "./notes.js";
import { People } from "./people.js";
import { DebugForm } from "./debug.js";

function main() {
  new People();
  new Notes();
  if (document.querySelector(".debug-card")) {
    const debug = new DebugForm();
    debug.showResponse("");
  }
}

main();