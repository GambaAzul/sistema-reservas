exports.handler = async (event) => {
  const name = event && event.name ? event.name : "sinnombre";

  return {
    statusCode: 200,
    body: JSON.stringify({ message: `hola testito ${name}` }),
  };
};
