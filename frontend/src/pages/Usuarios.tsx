import React, { useState } from "react";
import axios from "axios";

const Usuarios = () => {
  const [form, setForm] = useState({
    nombre: "",
    apellido: "",
    cargo: "",
    correo: "",
    celular: "",
    perfil: "usuario"
  });

  const [mensaje, setMensaje] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      await axios.post("/usuarios", form);
      setMensaje("✅ Usuario registrado correctamente");
    } catch (err: any) {
      setMensaje(`❌ ${err.response?.data?.detail || "Error al registrar usuario"}`);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Registro de Usuario</h1>

      {Object.keys(form).map((key) => (
        <div key={key} className="mb-3">
          <label className="block capitalize mb-1">{key}</label>
          <input
            type="text"
            name={key}
            value={(form as any)[key]}
            onChange={handleChange}
            className="w-full p-2 border rounded"
          />
        </div>
      ))}

      <button
        onClick={handleSubmit}
        className="bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700"
      >
        Registrar
      </button>

      {mensaje && <p className="mt-4 font-semibold">{mensaje}</p>}
    </div>
  );
};

export default Usuarios;
