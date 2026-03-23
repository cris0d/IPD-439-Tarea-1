# Tarea 1: Transferencia de Datos y Análisis de Desempeño (DMA vs CPU)
**Asignatura:** IPD439 - Seminario Avanzado de Computadores
**Institución:** Universidad Técnica Federico Santa María  
**Alumno:** Cristián Ayancán  
**Plataforma:** STM32L476RG (Nucleo-64)

## Descripción del Proyecto
Este repositorio contiene la implementación y el análisis de desempeño de diferentes métodos de transferencia de datos en un microcontrolador STM32L476. Se evalúa el tiempo de ejecución comparando la copia por software (`memcpy`) frente al uso del controlador de acceso directo a memoria (DMA).

## Estructura del Repositorio
* **Pregunta_1/**: Proyecto de STM32CubeIDE que evalúa transferencias SRAM $\to$ SRAM  y  FLASH $\to$ SRAM para bloques de 32 a 1024 bytes.
* **Pregunta_2/**: [Breve descripción de tu pregunta 2].

## Instrucciones para Replicar el Proyecto

### Importación en STM32CubeIDE
1. Clonar el repositorio: `git clone https://github.com/cris0d/IPD-439-Tarea-1.git`
2. Abrir STM32CubeIDE y seleccionar un nuevo Workspace.
3. Ir a `File > Import... > General > Existing Projects into Workspace`.
4. Seleccionar la carpeta `Pregunta_1` o `Pregunta_2`.
