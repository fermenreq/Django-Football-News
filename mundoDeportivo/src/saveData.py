#encoding: utf-8

import tkMessageBox
import urllib2
from bs4 import BeautifulSoup
import os
import django
from pip._vendor.pyparsing import unicodeString
import unicodedata
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
django.setup()
from mundoDeportivo.models import * 

#url = 'http://as.com/tag/copa_america/a/'
url = 'http://www.mundodeportivo.com'

def scraping(url):
    try:
        f = urllib2.urlopen(url)
        s = f.read()
        soup = BeautifulSoup(s,'html.parser')
        return soup
    except urllib2.HTTPError, e:
        entra = True
        paginaError= "CODIDO DE ERROR: "
        print paginaError,e.code
        #tkMessageBox.showinfo("ERROR",paginaError)
        return scraping(url)
    except urllib2.URLError,e:
        paginaError="Ocurrió un error en la url. Comprueba si tienes conexión"
        print "Ocurrió un error en la url. Comprueba si tienes conexión",e.message
        tkMessageBox.showinfo("ERROR",paginaError)


def explore():
    res = "Exploracion terminada"
    tamPaginas = 0
    soup = scraping(url)
    equipos = soup.find_all(class_='shield-teams-item')
    listaEquipos = []
    for x in equipos:
         for j in x.findAll('a'):
            enlace = j.get('href')
            listaEquipos.append(enlace)
    cont = 0
    tamBusquedaPaginasEquipos = len(listaEquipos)
        
    while cont < tamBusquedaPaginasEquipos:
        soup = scraping(listaEquipos[cont])
        paginaExtendidaEnlace = soup.find(class_='viewmore-button').get('href')
        pg = paginaExtendidaEnlace.split('/')[1:3]
        existePagina = True
        print "_________________________________________________________________________________________________________"
        print "Analizando Pagina: . . . . ", listaEquipos[cont]
        print "_________________________________________________________________________________________________________"
        indexPagina = 1
        
        #Obtener y guardar nombres equipo
        divsNombre = soup.find_all(class_='section-block-header')    
        for nombre in divsNombre:   
            titulo = nombre.find(class_='section-block-title-link').getText()
            print titulo
            modeloEquipo = Equipo(nombreEquipo = titulo)
            modeloEquipo.save() 

        while existePagina:
            #obtenemos url con vista completa
            enlacePaginaDatosCompleta = pg[0]+'/'+pg[1]+'/'+'p'+str(indexPagina)
            enlace = url+'/'+enlacePaginaDatosCompleta
            soup = scraping(enlace)
            paginacion = soup.find_all(class_='viewmore-pagination-item visible-md ')
            indiceUltimaPagina = ''

            #obtenemos numero de paginas totales del equipo
            for i in paginacion:
                indiceUltimaPagina = i.find('a').get('href')
            tamPagina = indiceUltimaPagina.split('p')[1]
            tam = int(tamPagina)
            tamPaginas=int(tam)
            #Descomentame para explorar 2 paginas por equipo
            tamPaginas = 2
            
            #procesamos informacion, por cada equipo exploramos sus atributos y guardamos
            divs = soup.find_all(class_='home-sections-body')
            for i in divs:
                #print "Analizando equipo: ", tituloEquipo
                link = i.find_all(class_='story-bottom')
                for l in link:
                    titulo= l.find(class_='story-header-title').getText()
                    urlNoticia= l.find(class_='story-header-title-link article-link').get('href')
                    fecha = l.find(class_='story-date').getText()
                    aux = fecha.split('/')
                    procesaFecha = aux[2]+'-'+aux[1]+'-'+aux[0]
                    #print tituloNoticia
                    #print enlaceNoticia
                    #print fecha
                    if l.find(class_='story-summary'):
                        texto = l.find(class_='story-summary').getText()
                        #print texto
                    else:
                        continue
                    
                    modeloNoticia = Noticia(nombreEquipo = modeloEquipo,
                                    tituloNoticia = titulo, 
                                    enlace = urlNoticia, 
                                    fecha = procesaFecha, noticia = texto)
                    modeloNoticia.save() 
                    
            print "Guardando datos . . . "
            
            indexPagina+=1
            #print indexPagina
            if indexPagina == tamPaginas:
                existePagina = False
        print cont
        cont = cont+1
    print "la paginacion por cada equipo ha sido de: "+str(tamPaginas)+' paginas por equipo'
    return res


def programaPrincipal():
    res = explore()
    print res

if __name__ == "__main__":
    print "LEEME:"
    print "************************************************************************************************************************************"
    print "Con este script realizamos scraping sobre la URL: "+url+"."
    print "Consiste en explorar y obtener todas las noticias de FUTBOL de todos los equipos que aloja el servidor, " \
          "es decir, hacemos uso de paginación. El objetivo de dicho Script, es poblar la BBDD de nuestra aplicaión web"
    print "Los valores que obtenemos hacen referencia a: Nombre del equipo, titulo de la noticia, enlace y noticia"
    print "***********************************************************************************************************************************"
    print ""
    print "IMPORTANTE:"
    print "***********************************************************************************************************************************"
    print "Durante la ejecucion de dicho scripts, se preven errores 504, Error HTTP 504 Gateway timeout (Tiempo de espera de gateway superado)."
    print "Para tratar dicho error, volvemos a ejecutar nuestro script sobre dicha pagina."
    print ""
    print ""
    print "Si deseas modificar el numero de paginacion por cada equipo, modifica la variable 'tamPaginas = ?' (linea 81)" \
          " por un valor comprendido entre [1 - 83]"
    print "Segun el tamaño de la paginacion tardará mas o menos, .... --> Paciencia, son muchos datos!. =) "

    programaPrincipal()