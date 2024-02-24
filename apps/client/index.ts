import { FastApiDemoClient } from "./generated";

const client = new FastApiDemoClient({
  BASE: "http://127.0.0.1:8000",
});

console.log("Calling API server");
const hello = await client.root.readRootGet();

console.log(hello);

const items = await client.items.getItemsItemsGet();

console.log(items);

