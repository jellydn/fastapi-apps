import { FastApiDemoClient } from "./generated";

/**
 * This function generates the client for interacting with the FastAPI server.
 */
const generate_client = async () => {
  const client = new FastApiDemoClient({
    BASE: "http://127.0.0.1:8000",
  });

  console.log("Calling API server");
  const hello = await client.root.readRootGet();

  console.log(hello);

  const items = await client.items.getItemsItemsGet();

  console.log(items);
};

generate_client();

