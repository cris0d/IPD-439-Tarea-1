# Tarea 1: Transferencia de Datos y Análisis de Desempeño (DMA vs CPU)
**Asignatura:** IPD439 - Seminario Avanzado de Computadores  
**Institución:** Universidad Técnica Federico Santa María  
**Alumno:** Cristián Ayancán  
**Plataforma:** STM32L476RG (Nucleo-64)

---

## Descripción del Proyecto
Este repositorio presenta la implementación y evaluación de distintos métodos de transferencia de datos en el microcontrolador STM32L476, comparando el uso de la CPU y el controlador DMA.

El trabajo se divide en dos partes principales:

- **Transferencias de memoria**, donde se analiza el desempeño de `memcpy` frente a DMA bajo distintas condiciones.
- **Sistema de adquisición de datos con ADC**, donde se compara el uso de interrupciones versus DMA para la captura de señales en tiempo real.

El objetivo es analizar el impacto de cada enfoque en el uso de la CPU y determinar en qué escenarios el uso de DMA resulta más conveniente.

---

## Estructura del Repositorio

### 📁 Pregunta_1/
Proyecto de STM32CubeIDE que evalúa transferencias de memoria:
- SRAM → SRAM  
- FLASH → SRAM  

Se analizan distintos tamaños de bloque (32 a 1024 bytes), comparando:
- CPU (`memcpy`)
- DMA

---

### 📁 Pregunta_2/
Implementación de un sistema de adquisición de datos utilizando el ADC del STM32.

Características principales:
- Captura de señales analógicas en el rango de **1 a 10 Hz**
- Frecuencia de muestreo de **1000 Hz**
- Buffer de **2000 muestras (2 segundos)**
- Comparación de dos métodos:
  - CPU mediante interrupciones
  - DMA para transferencia automática a memoria

Incluye:
- Envío de datos por puerto serial
- Script en Python para graficar y validar las señales adquiridas

---

## Instrucciones para Replicar el Proyecto

### 🔹 Clonar repositorio
```bash
1. git clone https://github.com/cris0d/IPD-439-Tarea-1.git
2. Abrir STM32CubeIDE y seleccionar un nuevo Workspace.
3. Ir a `File > Import... > General > Existing Projects into Workspace`.
4. Seleccionar la carpeta `Pregunta_1` o `Pregunta_2`.


## Configuración de Ejecución

En ambos proyectos (`Pregunta_1` y `Pregunta_2`), es necesario seleccionar el método de transferencia que se desea evaluar:

- **CPU**
- **DMA**

Para ello, se deben comentar o descomentar las secciones de código correspondientes, identificadas como:

//-------- CPU --------   o   //-------- DMA --------
según el método que se quiera utilizar para realizar las mediciones.
