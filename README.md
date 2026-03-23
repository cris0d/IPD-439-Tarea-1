# Tarea 1: Transferencia de Datos y Análisis de Desempeño (DMA vs CPU)
**Asignatura:** IPD432 - Diseño Avanzado de Sistemas Digitales  
**Institución:** Universidad Técnica Federico Santa María  
**Alumno:** Cristián Ayancán  
**Plataforma:** STM32L476RG (Nucleo-64)

## Descripción del Proyecto
Este repositorio contiene la implementación y el análisis de desempeño de diferentes métodos de transferencia de datos en un microcontrolador STM32L476. Se evalúa el tiempo de ejecución comparando la copia por software (`memcpy`) frente al uso del controlador de acceso directo a memoria (DMA).

## Estructura del Repositorio
* **Pregunta_1/**: Proyecto de STM32CubeIDE que evalúa transferencias SRAM $\to$ SRAM y FLASH $\to$ SRAM para bloques de 32 a 1024 bytes.
* **Pregunta_2/**: [Breve descripción de tu pregunta 2].
* **Codigos_Graficos/**: Scripts en Python utilizados para la visualización de los datos experimentales.

## Análisis Técnico de Resultados

### Configuración del Sistema
- **Frecuencia de Reloj (HCLK):** 80 MHz.
- **Latencia de Flash:** 3 Wait States (según RM0432, Tabla 12).
- **Herramientas:** STM32CubeIDE, Matplotlib/Seaborn para gráficos.

### Conclusiones Principales
1. **Impacto de la Jerarquía de Memoria:** Las transferencias desde Flash presentan una penalización de tiempo debido a los estados de espera requeridos a 80 MHz. La SRAM, al operar con latencia cero, permite un desempeño superior.
2. **Efectividad del DMA:** - En **SRAM $\to$ SRAM**, el DMA supera a la CPU para bloques $\ge$ 512 bytes al amortizar el *overhead* de configuración.
   - En **FLASH $\to$ SRAM**, el DMA resulta menos eficiente que la CPU debido a que esta última utiliza el **ART Accelerator** (caché), ventaja que el DMA no aprovecha de la misma forma.



## Instrucciones para Replicar el Proyecto

### Importación en STM32CubeIDE
1. Clonar el repositorio: `git clone https://github.com/TU_USUARIO/TU_REPO.git`
2. Abrir STM32CubeIDE y seleccionar un nuevo Workspace.
3. Ir a `File > Import... > General > Existing Projects into Workspace`.
4. Seleccionar la carpeta `Pregunta_1` o `Pregunta_2`.
5. **Importante:** Asegurarse de que "Copy projects into workspace" esté **desmarcado**.

### Generación de Gráficos (Python)
Para visualizar los resultados, es necesario instalar las dependencias:
```bash
pip install matplotlib numpy seaborn