#!/usr/bin/python

import os

for root, dirs, files in os.walk("."):
    for file in files:
        print(root + "\\" + file)
        if (file.find("java")!=-1 and file.find("formated")==-1):
            f = open(root + "\\" + file,'r')
            w = open(root + "\\" + file+'.formated','w')
            contenido = f.read().split('\n')
            f.close()            
            lineas=[]
            enComentario = False
            for l in contenido:
                if enComentario:
                    if l.find('*/')!=-1:
                        enComentario=False
                if enComentario == False:
                    if l.find('//')==-1 and l.find('/*')==-1:
                        lineas.append(l)
                    else:
                        if l.find('/*'):
                            enComentario=True
                            if l.find('*/'):
                                enComentario=False
            # contenido = contenido.replace('\n',' ')
            # contenido = contenido.replace('\r',' ')
            # contenido = contenido.replace('\t',' ')
            # while contenido.find('  ')!=-1:
                # contenido=contenido.replace('  ',' ')
            # enComentario = false
            # laLinea = ''
            # i=0
            # for c in contenido:
                # if c=='/':
                # i = i + 1
                # if enComentario:
                    # if finalComentarioSaltoLinea = False:
                        # if l[i:i+1]=='*/':
                            # enComentario = False
                        
                # if c=='/':
                    # if l[i:i+1]=='//':
                        # enComentario = true
                        # finalComentarioSaltoLinea = True
                        # laLinea = laLinea + c
                    # elif l[i:i+1]=='/*':
                        # enComentario = true
                        # finalComentarioSaltoLinea = False
                    # else:
                        # laLinea = laLinea + c
                            
                # w.write(l+'\n')
            todo = ''.join(lineas)
            todo = todo.replace('\n',' ')
            todo = todo.replace('\r',' ')
            todo = todo.replace('\t',' ')
            while todo.find('  ')!=-1:
                todo=todo.replace('  ',' ')
            lineas=[]
            l=''
            for c in todo:
                l=l+c;
                if c in ('{};'):
                    l=l.strip()
                    lineas.append(l)
                    l=''
            for l in lineas:
                w.write(l+'\n')
            w.close()