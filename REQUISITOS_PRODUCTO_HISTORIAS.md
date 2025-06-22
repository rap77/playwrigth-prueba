# Historias de Usuario Detalladas

## 👥 Epic 0: Extracción y Normalización de Datos (Scraping)

### US-000: Extracción de Datos de Vehículos
**Como** administrador del sistema  
**Quiero** extraer y almacenar datos de vehículos de Facebook Marketplace  
**Para** poblar la base de datos y habilitar el análisis posterior

**Criterios de Aceptación:**
- El sistema debe extraer datos de vehículos con scraping automatizado
- Cada vehículo debe tener un identificador único/hash
- Los datos deben insertarse en la base de datos evitando duplicados
- El sistema debe registrar la fecha de extracción
- Debe respetar robots.txt y términos de servicio

**Estimación**: 21 story points

### US-001: Actualización Periódica de Datos
**Como** administrador del sistema  
**Quiero** actualizar periódicamente los datos de vehículos  
**Para** mantener la información actualizada y detectar nuevos vehículos

**Criterios de Aceptación:**
- El sistema debe ejecutar scraping de forma programada (diaria/semanal)
- Solo se deben insertar vehículos nuevos (no duplicados)
- Los vehículos no encontrados en nuevas extracciones deben marcarse como inactivos
- El sistema debe registrar logs de actualización
- Debe manejar errores de red y reintentos automáticos

**Estimación**: 13 story points

### US-002: Resolución de Captchas por Usuario
**Como** administrador del sistema  
**Quiero** resolver captchas manualmente cuando aparezcan durante el scraping  
**Para** mantener el proceso de extracción funcionando

**Criterios de Aceptación:**
- El sistema debe detectar automáticamente cuando aparece un captcha
- Debe enviar notificación inmediata al administrador (email, chat, push)
- El administrador debe poder resolver el captcha desde la interfaz
- El proceso de scraping debe continuar automáticamente después de resolver
- Debe registrar todos los captchas resueltos para análisis

**Estimación**: 8 story points

---

## 👥 Epic 1: Ecommerce Público de Vehículos

### US-003: Catálogo Público de Vehículos
**Como** comprador potencial  
**Quiero** ver todos los vehículos disponibles en la plataforma  
**Para** encontrar el vehículo que necesito

**Criterios de Aceptación:**
- Debo poder ver vehículos de todos los concesionarios registrados
- El sistema debe mostrar imágenes, precio, especificaciones básicas
- Debo poder filtrar por marca, modelo, año, precio, ubicación
- El sistema debe mostrar información del concesionario vendedor
- Debo poder contactar directamente al vendedor

**Estimación**: 13 story points

### US-004: Buscador Avanzado de Vehículos
**Como** comprador con requisitos específicos  
**Quiero** buscar vehículos con filtros detallados  
**Para** encontrar exactamente lo que necesito

**Criterios de Aceptación:**
- Debo poder filtrar por rango de precios, años, millas
- El sistema debe permitir búsqueda por marca, modelo, color
- Debo poder especificar tipo de combustible (diesel, gasolina, eléctrico)
- El sistema debe permitir búsqueda por tipo de vehículo (sedan, camioneta, van, coupe, hatchback)
- Debo poder buscar por ubicación (estado, ciudad, zip code, área)
- El sistema debe permitir búsquedas guardadas

**Estimación**: 21 story points

### US-005: Comparador de Precios
**Como** comprador inteligente  
**Quiero** comparar precios de vehículos similares  
**Para** tomar la mejor decisión de compra

**Criterios de Aceptación:**
- Debo poder comparar hasta 5 vehículos lado a lado
- El sistema debe mostrar diferencias de precio, especificaciones y ubicación
- Debo poder ver análisis de si el precio está por encima/abajo del mercado
- El sistema debe sugerir vehículos similares para comparar
- Debo poder exportar comparaciones en PDF

**Estimación**: 17 story points

### US-006: Proceso de Compra Simplificado
**Como** comprador  
**Quiero** completar la compra de forma sencilla  
**Para** adquirir mi vehículo sin complicaciones

**Criterios de Aceptación:**
- Debo poder solicitar información adicional del vehículo
- El sistema debe permitir programar test drive
- Debo poder hacer ofertas o negociar precio
- El sistema debe facilitar el contacto con el vendedor
- Debo poder guardar vehículos favoritos

**Estimación**: 13 story points

---

## 👥 Epic 2: Gestión de Concesionarios y Vendedores

### US-007: Registro y Gestión de Concesionarios
**Como** concesionario  
**Quiero** registrar mi negocio en la plataforma  
**Para** vender mis vehículos al público

**Criterios de Aceptación:**
- Debo poder crear perfil de concesionario con información completa
- El sistema debe verificar mi licencia comercial
- Debo poder subir documentos de verificación
- El sistema debe permitir múltiples usuarios por concesionario
- Debo poder personalizar mi perfil y branding

**Estimación**: 8 story points

### US-008: Gestión de Inventario de Vehículos
**Como** concesionario  
**Quiero** gestionar mi inventario de vehículos  
**Para** mantener mi catálogo actualizado

**Criterios de Aceptación:**
- Debo poder agregar vehículos con especificaciones detalladas
- El sistema debe permitir importar inventario desde CSV/Excel
- Debo poder editar, activar/desactivar vehículos
- El sistema debe calcular precio sugerido basado en análisis de mercado
- Debo poder marcar vehículos como vendidos o reservados
- El sistema debe permitir subir múltiples imágenes por vehículo

**Estimación**: 17 story points

### US-009: Dashboard de Vendedor
**Como** vendedor/concesionario  
**Quiero** ver métricas de mis ventas y vehículos  
**Para** optimizar mi estrategia de ventas

**Criterios de Aceptación:**
- Debo poder ver estadísticas de visitas a mis vehículos
- El sistema debe mostrar tiempo promedio de venta por vehículo
- Debo poder ver análisis de precios vs competencia
- El sistema debe mostrar leads generados y conversiones
- Debo poder ver reportes de rendimiento mensual/anual

**Estimación**: 13 story points

---

## 👥 Epic 3: Análisis de Precios y Mercado

### US-010: Análisis de Precios de Mercado
**Como** vendedor  
**Quiero** saber si mis precios están competitivos  
**Para** maximizar mis ventas y ganancias

**Criterios de Aceptación:**
- El sistema debe identificar si vendo por encima/abajo del mercado
- Debo poder ver precio promedio, mediana y percentiles del mercado
- El sistema debe mostrar análisis por marca, modelo, año, millas
- Debo poder ver tendencias de precios en el tiempo
- El sistema debe sugerir precio óptimo basado en análisis de mercado

**Estimación**: 21 story points

### US-011: Detección de Oportunidades de Compra
**Como** concesionario  
**Quiero** identificar vehículos con precios por debajo del mercado  
**Para** encontrar oportunidades de compra y reventa

**Criterios de Aceptación:**
- El sistema debe detectar vehículos con precios anómalos
- Debo poder ver score de oportunidad por vehículo
- El sistema debe alertar sobre vehículos urgentes de vender
- Debo poder configurar criterios de búsqueda de oportunidades
- El sistema debe mostrar análisis de potencial de ganancia

**Estimación**: 17 story points

### US-012: Búsquedas Avanzadas para Clientes
**Como** vendedor  
**Quiero** buscar vehículos según requisitos específicos de clientes  
**Para** encontrar exactamente lo que necesitan

**Criterios de Aceptación:**
- Debo poder hacer búsquedas generales (rango de años, marcas, tipos)
- El sistema debe permitir búsquedas específicas (modelo exacto, especificaciones)
- Debo poder guardar búsquedas frecuentes de clientes
- El sistema debe alertar cuando aparezcan vehículos que coincidan
- Debo poder compartir resultados de búsqueda con clientes

**Estimación**: 13 story points

---

## 👥 Epic 4: Gestión de Publicaciones en Redes Sociales

### US-013: Control de Publicaciones en Redes Sociales
**Como** vendedor  
**Quiero** gestionar las publicaciones de mis vehículos en redes sociales  
**Para** maximizar la visibilidad de mi inventario

**Criterios de Aceptación:**
- Debo poder ver qué vehículos están publicados en cada red social
- El sistema debe mostrar cuántas veces se ha publicado cada vehículo
- Debo poder identificar vehículos nuevos que no se han publicado
- El sistema debe permitir programar publicaciones automáticas
- Debo poder ver métricas de engagement por publicación

**Estimación**: 21 story points

### US-014: Fuerza de Ventas Digital
**Como** concesionario  
**Quiero** que mi equipo de ventas publique vehículos en sus redes  
**Para** ampliar el alcance de mis ventas

**Criterios de Aceptación:**
- Debo poder asignar vehículos a vendedores específicos
- El sistema debe generar contenido optimizado para cada red social
- Debo poder ver qué vendedor publicó cada vehículo
- El sistema debe trackear leads generados por cada vendedor
- Debo poder configurar comisiones por ventas generadas

**Estimación**: 17 story points

### US-015: Detección de Precios Engañosos
**Como** administrador del sistema  
**Quiero** detectar publicaciones con precios engañosos  
**Para** mantener la calidad de la plataforma

**Criterios de Aceptación:**
- El sistema debe detectar precios de inicial vs precio total
- Debo poder marcar publicaciones como engañosas
- El sistema debe alertar sobre discrepancias en precios
- Debo poder establecer reglas de validación de precios
- El sistema debe permitir moderación manual de publicaciones

**Estimación**: 13 story points

---

## 👥 Epic 5: Sistema de Suscripciones y Monetización

### US-016: Planes de Suscripción Flexibles
**Como** administrador del SaaS  
**Quiero** ofrecer diferentes planes según necesidades  
**Para** maximizar la adopción y revenue

**Criterios de Aceptación:**
- Debo poder crear planes mensuales y anuales con descuento
- El sistema debe ofrecer período de prueba gratuito
- Debo poder establecer límites por volumen de vehículos
- El sistema debe permitir upgrades/downgrades de planes
- Debo poder configurar funcionalidades premium por plan

**Estimación**: 13 story points

### US-017: Comisiones por Ventas
**Como** administrador de la plataforma  
**Quiero** cobrar comisiones por ventas realizadas  
**Para** generar revenue adicional

**Criterios de Aceptación:**
- Debo poder configurar porcentajes de comisión por categoría
- El sistema debe trackear ventas y calcular comisiones automáticamente
- Debo poder generar facturas de comisiones
- El sistema debe permitir diferentes modelos de comisión
- Debo poder ver reportes de revenue por comisiones

**Estimación**: 8 story points

---

## 👥 Epic 6: Inteligencia Artificial y Automatización

### US-018: Agente IA de Ventas
**Como** vendedor  
**Quiero** un asistente IA que me ayude con las ventas  
**Para** aumentar mis conversiones y eficiencia

**Criterios de Aceptación:**
- El agente IA debe responder preguntas básicas sobre productos
- Debe sugerir productos basado en preferencias del cliente
- Debe poder programar test drives automáticamente
- Debe escalar a agente humano cuando sea necesario
- Debe aprender de las interacciones para mejorar

**Estimación**: 21 story points

### US-019: Recomendaciones IA Personalizadas
**Como** comprador  
**Quiero** recibir recomendaciones personalizadas de vehículos  
**Para** encontrar opciones que se ajusten a mis necesidades

**Criterios de Aceptación:**
- El sistema debe analizar mi comportamiento de navegación
- Debe considerar mi historial de búsquedas y favoritos
- Debe sugerir vehículos similares a los que he visto
- Debe adaptar las recomendaciones según mis interacciones
- Debe explicar por qué me sugiere cada vehículo

**Estimación**: 17 story points

### US-020: Análisis Predictivo de Precios
**Como** vendedor  
**Quiero** predicciones de precios basadas en IA  
**Para** establecer precios óptimos para mis vehículos

**Criterios de Aceptación:**
- El sistema debe predecir precios futuros basado en tendencias
- Debe considerar factores como estacionalidad y demanda
- Debe alertar sobre cambios significativos en el mercado
- Debe sugerir el mejor momento para vender
- Debe explicar los factores que influyen en las predicciones

**Estimación**: 21 story points

### US-021: Chatbot Omnicanal
**Como** usuario de la plataforma  
**Quiero** recibir atención a través de múltiples canales  
**Para** obtener ayuda cuando y donde la necesite

**Criterios de Aceptación:**
- El chatbot debe estar disponible en web, WhatsApp, Facebook Messenger
- Debe mantener contexto de conversación entre canales
- Debe poder resolver consultas básicas automáticamente
- Debe escalar a agente humano cuando sea necesario
- Debe integrarse con el sistema de tickets y CRM

**Estimación**: 17 story points

---

## 📊 Resumen de Estimaciones

| Epic | Story Points | Prioridad |
|------|-------------|-----------|
| Epic 0: Scraping | 42 | Crítica |
| Epic 1: Ecommerce | 64 | Alta |
| Epic 2: Gestión Dealers | 38 | Alta |
| Epic 3: Análisis | 51 | Media |
| Epic 4: Redes Sociales | 51 | Media |
| Epic 5: Monetización | 21 | Alta |
| Epic 6: IA | 76 | Media |

**Total Story Points**: 343

---

*Documento de Historias de Usuario - Versión 4.0* 