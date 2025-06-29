const { handler } = require("./index.js");

describe("Handler Lambda", () => {
  it("debería devolver saludo con el nombre proporcionado", async () => {
    const evento = { name: "Testito" };
    const esperado = JSON.stringify({ message: "hola testito Testito" });

    const resultado = await handler(evento);

    expect(resultado.body).toBe(esperado);
  });

  it("debería devolver saludo con nombre por defecto si no se proporciona", async () => {
    const evento = {};
    const esperado = JSON.stringify({ message: "hola testito sinnombre" });

    const resultado = await handler(evento);

    expect(resultado.body).toBe(esperado);
  });

  it("debería devolver statusCode 200", async () => {
    const evento = {};
    const resultado = await handler(evento);
    expect(resultado.statusCode).toBe(200);
  });

  it("debería manejar evento null sin fallar", async () => {
    const resultado = await handler(null);
    expect(resultado.body).toBe(JSON.stringify({ message: "hola testito sinnombre" }));
  });

  it("debería manejar evento undefined sin fallar", async () => {
    const resultado = await handler(undefined);
    expect(resultado.body).toBe(JSON.stringify({ message: "hola testito sinnombre" }));
  });
});
