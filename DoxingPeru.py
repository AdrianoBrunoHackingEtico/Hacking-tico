#coded by Adriano Bruno

import os
import sys
import platform
import subprocess
import webbrowser

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú de opciones."""
    limpiar_pantalla()

    print("""
\033[1;31m                       8b,dPPYba,   ,adPPYba, 8b,dPPYba, 88       88
\033[1;31m                       88P'    "8a a8P_____88 88P'   "Y8 88       88
\033[1;37m                       88       d8 8PP        88         88       88
\033[1;37m                       88b,   ,a8" "8b,   ,aa 88         "8a,   ,a88
\033[1;31m                       88`YbbdP"'   `"Ybbd8"' 88          `"YbbdP'Y8
\033[1;31m                       88
\033[1;31m                       88

				     \033[1;31m- HACKING ÉTICO -
			           \033[1;34mCODED BY:\033[1;m Adriano Bruno

\033[1;33mCada opción te brinda un sitio Web Oficial del Estado Peruano para que puedas buscar datos públicos
		básicos de personas. Úsalo con responsabilidad.
""")
    print ('''
\033[1;31m---------------------------------------------------------------------------------------------------
\033[1;32m 1. Dni 	   \033[1;32m 5. Sis         \033[1;32m 9. Recibo luz    \033[1;32m  13. Deuda alimenticia    \033[1;32m 17. Denuncias
\033[1;32m 2. Trámite Dni    \033[1;32m 6. Susalud    \033[1;32m 10. Minedu       \033[1;32m   14. Deuda tributaria     \033[1;32m 18. Antecedentes
\033[1;32m 3. Censo      	   \033[1;32m 7. Juntos    \033[1;32m  11. Licencia     \033[1;32m   15. Multas JNE  	        \033[1;32m 19. Acerca de
\033[1;32m 4. Teléfono       \033[1;32m 8. Ruc        \033[1;32m 12. Migraciones    \033[1;32m 16. Papeletas        \033[1;32m     20. Salir
\033[1;31m---------------------------------------------------------------------------------------------------
		''')

def mostrar_info():
    """Muestra información sobre el programa."""
    limpiar_pantalla()

    print("""
\033[1;31m                       - Información sobre el programa -

\033[1;37mEste proyecto esta hecho con fin educativo. El objetivo principal es obtener datos sobre personas
que hayan sido identificados como acosadores o agresores dentro del contexto del estado peruano. Además es
importante destacar que este proyecto se llevará a cabo con total transparencia y en cumplimiento estricto
de las leyes y regulaciones vigentes en materia de protección de datos y derechos humanos.

\033[1;34mVersión:\033[1;m Beta 1.0
\033[1;34mAutor:\033[1;m Adriano Bruno
\033[1;34mContacto:\033[1;m adriano@example.com
""")

    input("Presiona Enter para volver al menú principal...")

def abrir_enlace(enlace):
    """Abre el enlace en el navegador web."""
    webbrowser.open(enlace)

def ejecutar_consulta(opcion):
    """Ejecuta una consulta basada en la opción elegida por el usuario."""
    opciones = {
        "1": "https://serviciosweb.reniec.gob.pe/aip/",
        "2": "https://serviciosportal.reniec.gob.pe/cetdnipi/inicio.htm",
        "3": "https://operaciones.sisfoh.gob.pe:450/cse/",
        "4": "https://checatuslineas.osiptel.gob.pe/",
        "5": "http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx",
        "6": "https://app1.susalud.gob.pe/registro/",
        "7": "http://aplicacionesweb2.juntos.gob.pe:7007/lr/rest/consulta/consulta-ciudadano-juntos",
        "8": "https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp",
        "9": "https://www.gob.pe/23534-consultar-recibo-de-luz",
        "10": "https://titulosinstitutos.minedu.gob.pe/",
        "11": "https://licencias.mtc.gob.pe/#/index",
        "12": "https://sel.migraciones.gob.pe/servmig-valreg/VerificarPAS",
        "13": "https://casillas.pj.gob.pe/redam/#/",
        "14": "https://www.sat.gob.pe/VirtualSAT/modulos/BusquedaTributario.aspx?mysession=eoyz9fLQuGihkJe0z0vy5WPILNVoMSZmbmp7GbQ54%2fE%3d&tri=T",
        "15": "https://multas.jne.gob.pe/login",
        "16": "https://www.sat.gob.pe/VirtualSAT/modulos/papeletas.aspx?mysession=eoyz9fLQuGihkJe0z0vy5WPILNVoMSZmbmp7GbQ54%2fE%3d",
        "17": "https://portal.mpfn.gob.pe/seguimiento-de-denuncias",
        "18": "https://www.gob.pe/33567-obtener-antecedentes-policiales-judiciales-y-penales",
        "19": mostrar_info,
        "20": exit
    }

    if opcion == "20":
        return False
    elif opcion in opciones:
        if opciones[opcion] == exit:
            return False
        elif opciones[opcion] == mostrar_info:
            mostrar_info()
            return True
        else:
            abrir_enlace(opciones[opcion])
            input("Presiona Enter para continuar...")
            return True
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
        input("Presiona Enter para continuar...")
        return True

def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("\033[1;30m Escribe el número a consultar (•.•)> ")

        if not ejecutar_consulta(opcion):
            break

if __name__ == "__main__":
    main()