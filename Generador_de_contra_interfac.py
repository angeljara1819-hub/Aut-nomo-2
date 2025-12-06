import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import time

class GeneradorContraseñasMejorado:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("🔐 Generador de Contraseñas Avanzado")
        self.ventana.geometry("750x700")
        self.ventana.configure(bg="#2c3e50")
        self.ventana.resizable(False, False)
        
        # Variables
        self.contraseña_generada = ""
        self.intentos_restantes = 3
        self.acceso_concedido = False
        self.historial = []
        
        # Configurar estilo
        self.configurar_estilos()
        self.crear_interfaz()
    
    def configurar_estilos(self):
        """Configura estilos para los widgets"""
        self.estilo = ttk.Style()
        self.estilo.configure("Titulo.TLabel", 
                            font=("Arial", 18, "bold"),
                            foreground="#3498db",
                            background="#2c3e50")
        
        self.estilo.configure("Subtitulo.TLabel",
                            font=("Arial", 12, "bold"),
                            foreground="#ecf0f1",
                            background="#34495e")
    
    def crear_interfaz(self):
        # Título principal con emoji
        titulo = tk.Label(
            self.ventana,
            text="🔐 GENERADOR DE CONTRASEÑAS AVANZADO",
            font=("Arial", 16, "bold"),
            fg="#3498db",
            bg="#2c3e50",
            pady=10
        )
        titulo.pack(fill="x")
        
        # Frame principal con pestañas
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Pestaña 1: Generador
        self.tab_generador = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_generador, text="🚀 Generar Contraseña")
        
        # Pestaña 2: Verificador
        self.tab_verificador = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_verificador, text="🔍 Verificar Acceso")
        
        # Pestaña 3: Historial
        self.tab_historial = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_historial, text="📊 Historial")
        
        self.crear_tab_generador()
        self.crear_tab_verificador()
        self.crear_tab_historial()
        
        # Barra de estado
        self.barra_estado = tk.Label(
            self.ventana,
            text="Listo - Seleccione un nivel de seguridad",
            font=("Arial", 9),
            fg="#bdc3c7",
            bg="#34495e",
            relief="sunken",
            bd=1
        )
        self.barra_estado.pack(fill="x", side="bottom")
    
    def crear_tab_generador(self):
        """Crea la interfaz de la pestaña generador"""
        # Frame de configuración
        frame_config = tk.Frame(self.tab_generador, bg="#34495e", relief="raised", bd=2)
        frame_config.pack(pady=10, padx=15, fill="x")
        
        tk.Label(
            frame_config,
            text="Configuración de Contraseña",
            font=("Arial", 14, "bold"),
            fg="#ecf0f1",
            bg="#34495e"
        ).pack(pady=10)
        
        # Opciones de personalización
        frame_opciones = tk.Frame(frame_config, bg="#34495e")
        frame_opciones.pack(pady=10)
        
        # Longitud
        tk.Label(frame_opciones, text="Longitud:", fg="#ecf0f1", bg="#34495e", font=("Arial", 10)).grid(row=0, column=0, padx=5, sticky="w")
        self.longitud_var = tk.IntVar(value=8)
        self.spin_longitud = tk.Spinbox(frame_opciones, from_=4, to=20, width=5, textvariable=self.longitud_var, font=("Arial", 10))
        self.spin_longitud.grid(row=0, column=1, padx=5)
        
        # Incluir mayúsculas
        self.mayusculas_var = tk.BooleanVar(value=True)
        tk.Checkbutton(frame_opciones, text="Incluir Mayúsculas", variable=self.mayusculas_var, 
                      fg="#ecf0f1", bg="#34495e", selectcolor="#2c3e50", font=("Arial", 9)).grid(row=0, column=2, padx=10)
        
        # Incluir números
        self.numeros_var = tk.BooleanVar(value=True)
        tk.Checkbutton(frame_opciones, text="Incluir Números", variable=self.numeros_var,
                      fg="#ecf0f1", bg="#34495e", selectcolor="#2c3e50", font=("Arial", 9)).grid(row=1, column=2, padx=10)
        
        # Incluir símbolos
        self.simbolos_var = tk.BooleanVar(value=False)
        tk.Checkbutton(frame_opciones, text="Incluir Símbolos", variable=self.simbolos_var,
                      fg="#ecf0f1", bg="#34495e", selectcolor="#2c3e50", font=("Arial", 9)).grid(row=0, column=3, padx=10)
        
        # Botones de nivel rápido
        frame_botones_rapidos = tk.Frame(frame_config, bg="#34495e")
        frame_botones_rapidos.pack(pady=10)
        
        tk.Label(frame_botones_rapidos, text="Niveles rápidos:", fg="#ecf0f1", bg="#34495e", font=("Arial", 10)).pack(side="left", padx=5)
        
        tk.Button(frame_botones_rapidos, text="Básica", command=lambda: self.configurar_rapida("basica"),
                 bg="#e74c3c", fg="white", font=("Arial", 9), width=8).pack(side="left", padx=2)
        
        tk.Button(frame_botones_rapidos, text="Media", command=lambda: self.configurar_rapida("media"),
                 bg="#f39c12", fg="white", font=("Arial", 9), width=8).pack(side="left", padx=2)
        
        tk.Button(frame_botones_rapidos, text="Fuerte", command=lambda: self.configurar_rapida("fuerte"),
                 bg="#27ae60", fg="white", font=("Arial", 9), width=8).pack(side="left", padx=2)
        
        # Botón generar
        tk.Button(frame_config, text="🎲 GENERAR CONTRASEÑA PERSONALIZADA", 
                 command=self.generar_personalizada,
                 bg="#9b59b6", fg="white", font=("Arial", 11, "bold"),
                 width=30, height=2).pack(pady=15)
        
        # Área de contraseña generada
        frame_resultado = tk.Frame(self.tab_generador, bg="#34495e", relief="sunken", bd=2)
        frame_resultado.pack(pady=10, padx=15, fill="x")
        
        tk.Label(frame_resultado, text="Contraseña Generada:", font=("Arial", 12, "bold"),
                fg="#ecf0f1", bg="#34495e").pack(pady=8)
        
        self.lbl_contraseña_generada = tk.Label(
            frame_resultado,
            text="Haga clic en generar para crear una contraseña",
            font=("Courier", 14, "bold"),
            fg="#f1c40f",
            bg="#2c3e50",
            width=40,
            height=2,
            relief="solid",
            bd=1,
            wraplength=600
        )
        self.lbl_contraseña_generada.pack(pady=10, padx=10)
        
        # Botones de acción
        frame_acciones = tk.Frame(frame_resultado, bg="#34495e")
        frame_acciones.pack(pady=10)
        
        tk.Button(frame_acciones, text="📋 Copiar al Portapapeles", 
                 command=self.copiar_portapapeles, bg="#3498db", fg="white", font=("Arial", 9)).pack(side="left", padx=5)
        
        tk.Button(frame_acciones, text="💾 Guardar en Historial", 
                 command=self.guardar_historial, bg="#2ecc71", fg="white", font=("Arial", 9)).pack(side="left", padx=5)
        
        tk.Button(frame_acciones, text="👁️ Mostrar/Ocultar", 
                 command=self.toggle_visualizacion, bg="#e67e22", fg="white", font=("Arial", 9)).pack(side="left", padx=5)
        
        # Indicador de fortaleza
        self.lbl_fortaleza = tk.Label(frame_resultado, text="Fortaleza: --", font=("Arial", 10, "bold"),
                                     fg="#bdc3c7", bg="#34495e")
        self.lbl_fortaleza.pack(pady=5)
    
    def crear_tab_verificador(self):
        """Crea la interfaz de la pestaña verificador"""
        frame_verificador = tk.Frame(self.tab_verificador, bg="#34495e")
        frame_verificador.pack(pady=20, padx=15, fill="both", expand=True)
        
        tk.Label(frame_verificador, text="SISTEMA DE VERIFICACIÓN DE ACCESO", 
                font=("Arial", 16, "bold"), fg="#ecf0f1", bg="#34495e").pack(pady=15)
        
        # Indicador de intentos
        self.lbl_intentos = tk.Label(
            frame_verificador,
            text=f"🔐 Intentos restantes: {self.intentos_restantes}",
            font=("Arial", 14, "bold"),
            fg="#e67e22",
            bg="#34495e"
        )
        self.lbl_intentos.pack(pady=10)
        
        # Campo de contraseña
        tk.Label(frame_verificador, text="Ingrese la contraseña:", 
                font=("Arial", 11), fg="#ecf0f1", bg="#34495e").pack(pady=5)
        
        frame_entrada = tk.Frame(frame_verificador, bg="#34495e")
        frame_entrada.pack(pady=10)
        
        self.entrada_contraseña = tk.Entry(
            frame_entrada,
            font=("Arial", 12),
            width=30,
            show="•"
        )
        self.entrada_contraseña.pack(side="left", padx=5)
        self.entrada_contraseña.bind("<Return>", lambda e: self.verificar_acceso())
        
        self.btn_toggle_visual = tk.Button(frame_entrada, text="👁️", 
                                          command=self.toggle_visual_entrada,
                                          bg="#7f8c8d", fg="white", font=("Arial", 10), width=3)
        self.btn_toggle_visual.pack(side="left", padx=5)
        
        # Botón verificar
        self.btn_verificar = tk.Button(
            frame_verificador,
            text="✅ VERIFICAR ACCESO",
            command=self.verificar_acceso,
            bg="#2980b9",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            height=2
        )
        self.btn_verificar.pack(pady=15)
        
        # Resultado
        self.lbl_resultado = tk.Label(
            frame_verificador,
            text="Esperando verificación...",
            font=("Arial", 12),
            fg="#bdc3c7",
            bg="#34495e",
            wraplength=500
        )
        self.lbl_resultado.pack(pady=10)
        
        # Progreso
        self.progreso = ttk.Progressbar(frame_verificador, orient="horizontal", length=300, mode="determinate")
        self.progreso.pack(pady=10)
        
        # Botón reiniciar
        tk.Button(frame_verificador, text="🔄 Reiniciar Sistema", 
                 command=self.reiniciar_sistema, bg="#e74c3c", fg="white", font=("Arial", 10)).pack(pady=10)
    
    def crear_tab_historial(self):
        """Crea la pestaña de historial"""
        frame_historial = tk.Frame(self.tab_historial, bg="#34495e")
        frame_historial.pack(fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(frame_historial, text="📊 HISTORIAL DE CONTRASEÑAS GENERADAS", 
                font=("Arial", 14, "bold"), fg="#ecf0f1", bg="#34495e").pack(pady=10)
        
        # Treeview para el historial
        columns = ("Fecha", "Contraseña", "Longitud", "Fortaleza")
        self.tree_historial = ttk.Treeview(frame_historial, columns=columns, show="headings", height=12)
        
        # Configurar columnas
        for col in columns:
            self.tree_historial.heading(col, text=col)
            self.tree_historial.column(col, width=120)
        
        self.tree_historial.column("Contraseña", width=200)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_historial, orient="vertical", command=self.tree_historial.yview)
        self.tree_historial.configure(yscrollcommand=scrollbar.set)
        
        self.tree_historial.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botones de historial
        frame_botones_hist = tk.Frame(frame_historial, bg="#34495e")
        frame_botones_hist.pack(fill="x", pady=10)
        
        tk.Button(frame_botones_hist, text="🗑️ Limpiar Historial", 
                 command=self.limpiar_historial, bg="#e74c3c", fg="white", font=("Arial", 9)).pack(side="left", padx=5)
        
        tk.Button(frame_botones_hist, text="📋 Copiar Seleccionado", 
                 command=self.copiar_seleccionado, bg="#3498db", fg="white", font=("Arial", 9)).pack(side="left", padx=5)
        
        tk.Button(frame_botones_hist, text="💾 Exportar a Archivo", 
                 command=self.exportar_historial, bg="#2ecc71", fg="white", font=("Arial", 9)).pack(side="left", padx=5)
    
    def configurar_rapida(self, nivel):
        """Configura los parámetros según nivel rápido"""
        if nivel == "basica":
            self.longitud_var.set(6)
            self.mayusculas_var.set(False)
            self.numeros_var.set(False)
            self.simbolos_var.set(False)
        elif nivel == "media":
            self.longitud_var.set(8)
            self.mayusculas_var.set(True)
            self.numeros_var.set(True)
            self.simbolos_var.set(False)
        else:  # fuerte
            self.longitud_var.set(12)
            self.mayusculas_var.set(True)
            self.numeros_var.set(True)
            self.simbolos_var.set(True)
        
        self.actualizar_barra_estado(f"Configurado nivel {nivel}")
    
    def generar_personalizada(self):
        """Genera contraseña personalizada"""
        longitud = self.longitud_var.get()
        usar_mayusculas = self.mayusculas_var.get()
        usar_numeros = self.numeros_var.get()
        usar_simbolos = self.simbolos_var.get()
        
        # Construir conjunto de caracteres
        caracteres = string.ascii_lowercase
        if usar_mayusculas:
            caracteres += string.ascii_uppercase
        if usar_numeros:
            caracteres += string.digits
        if usar_simbolos:
            caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not caracteres:
            messagebox.showwarning("Advertencia", "Seleccione al menos un tipo de carácter")
            return
        
        # Generar contraseña
        self.contraseña_generada = ''.join(random.choice(caracteres) for _ in range(longitud))
        
        # Actualizar interfaz
        self.mostrar_contraseña_generada()
        
        # Calcular y mostrar fortaleza
        fortaleza = self.calcular_fortaleza()
        self.lbl_fortaleza.configure(text=f"Fortaleza: {fortaleza}")
        
        self.actualizar_barra_estado("Contraseña generada exitosamente")
    
    def calcular_fortaleza(self):
        """Calcula la fortaleza de la contraseña"""
        longitud = len(self.contraseña_generada)
        tiene_mayusculas = any(c.isupper() for c in self.contraseña_generada)
        tiene_numeros = any(c.isdigit() for c in self.contraseña_generada)
        tiene_simbolos = any(not c.isalnum() for c in self.contraseña_generada)
        
        puntaje = 0
        if longitud >= 12: puntaje += 3
        elif longitud >= 8: puntaje += 2
        elif longitud >= 6: puntaje += 1
        
        if tiene_mayusculas: puntaje += 1
        if tiene_numeros: puntaje += 1
        if tiene_simbolos: puntaje += 2
        
        if puntaje >= 5: return "MUY FUERTE 🛡️"
        elif puntaje >= 3: return "FUERTE 💪"
        elif puntaje >= 2: return "MEDIA ⚖️"
        else: return "DÉBIL ⚠️"
    
    def mostrar_contraseña_generada(self):
        """Muestra la contraseña generada con animación"""
        self.lbl_contraseña_generada.configure(text=self.contraseña_generada, fg="#2ecc71")
        
        # Efecto visual
        self.lbl_contraseña_generada.configure(bg="#27ae60")
        self.ventana.after(200, lambda: self.lbl_contraseña_generada.configure(bg="#2c3e50"))
    
    def copiar_portapapeles(self):
        """Copia la contraseña al portapapeles"""
        if self.contraseña_generada:
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(self.contraseña_generada)
            self.actualizar_barra_estado("Contraseña copiada al portapapeles")
            messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles")
        else:
            messagebox.showwarning("Advertencia", "No hay contraseña para copiar")
    
    def toggle_visualizacion(self):
        """Alterna entre mostrar y ocultar la contraseña"""
        current_text = self.lbl_contraseña_generada.cget("text")
        if current_text.startswith("*" * len(self.contraseña_generada)):
            self.lbl_contraseña_generada.configure(text=self.contraseña_generada)
        else:
            self.lbl_contraseña_generada.configure(text="*" * len(self.contraseña_generada))
    
    def toggle_visual_entrada(self):
        """Alterna visibilidad en campo de entrada"""
        if self.entrada_contraseña.cget("show") == "":
            self.entrada_contraseña.configure(show="•")
            self.btn_toggle_visual.configure(bg="#7f8c8d")
        else:
            self.entrada_contraseña.configure(show="")
            self.btn_toggle_visual.configure(bg="#3498db")
    
    def guardar_historial(self):
        """Guarda la contraseña actual en el historial"""
        if not self.contraseña_generada:
            messagebox.showwarning("Advertencia", "No hay contraseña para guardar")
            return
        
        fecha = time.strftime("%Y-%m-%d %H:%M:%S")
        fortaleza = self.calcular_fortaleza()
        
        self.historial.append({
            "fecha": fecha,
            "contraseña": self.contraseña_generada,
            "longitud": len(self.contraseña_generada),
            "fortaleza": fortaleza
        })
        
        self.actualizar_tree_historial()
        self.actualizar_barra_estado("Contraseña guardada en historial")
    
    def actualizar_tree_historial(self):
        """Actualiza el treeview del historial"""
        # Limpiar treeview
        for item in self.tree_historial.get_children():
            self.tree_historial.delete(item)
        
        # Agregar items
        for item in self.historial:
            self.tree_historial.insert("", "end", values=(
                item["fecha"],
                item["contraseña"],
                item["longitud"],
                item["fortaleza"]
            ))
    
    def verificar_acceso(self):
        """Verifica el acceso con animaciones"""
        if not self.contraseña_generada:
            messagebox.showwarning("Advertencia", "Primero genere una contraseña")
            return
        
        contraseña_ingresada = self.entrada_contraseña.get()
        
        # Animación de verificación
        self.progreso.start(10)
        self.lbl_resultado.configure(text="Verificando...", fg="#f39c12")
        
        self.ventana.after(1000, lambda: self.finalizar_verificacion(contraseña_ingresada))
    
    def finalizar_verificacion(self, contraseña_ingresada):
        """Finaliza el proceso de verificación"""
        self.progreso.stop()
        
        if contraseña_ingresada == self.contraseña_generada:
            self.acceso_concedido = True
            self.lbl_resultado.configure(text="🎉 ACCESO CONCEDIDO - ¡BIENVENIDO/A! 🎉", fg="#27ae60")
            self.lbl_intentos.configure(text="✅ ACCESO CONCEDIDO", fg="#27ae60")
            self.entrada_contraseña.configure(state="disabled")
            self.btn_verificar.configure(state="disabled")
            messagebox.showinfo("Éxito", "¡Acceso concedido! Bienvenido al sistema.")
        else:
            self.intentos_restantes -= 1
            self.lbl_intentos.configure(text=f"🔐 Intentos restantes: {self.intentos_restantes}")
            
            if self.intentos_restantes > 0:
                self.lbl_resultado.configure(
                    text=f"❌ Contraseña incorrecta. Te quedan {self.intentos_restantes} intento(s)",
                    fg="#e74c3c"
                )
            else:
                self.lbl_resultado.configure(text="🚫 ACCESO BLOQUEADO - Sistema bloqueado", fg="#c0392b")
                self.lbl_intentos.configure(text="🚫 ACCESO BLOQUEADO", fg="#c0392b")
                self.entrada_contraseña.configure(state="disabled")
                self.btn_verificar.configure(state="disabled")
                messagebox.showerror("Error", "Has agotado tus intentos. Acceso bloqueado.")
        
        self.entrada_contraseña.delete(0, "end")
    
    def reiniciar_sistema(self):
        """Reinicia el sistema de verificación"""
        self.intentos_restantes = 3
        self.acceso_concedido = False
        self.lbl_intentos.configure(text=f"🔐 Intentos restantes: {self.intentos_restantes}", fg="#e67e22")
        self.lbl_resultado.configure(text="Sistema reiniciado. Puede intentar nuevamente.", fg="#bdc3c7")
        self.entrada_contraseña.configure(state="normal")
        self.btn_verificar.configure(state="normal")
        self.entrada_contraseña.delete(0, "end")
        self.progreso.stop()
        self.actualizar_barra_estado("Sistema de verificación reiniciado")
    
    def copiar_seleccionado(self):
        """Copia la contraseña seleccionada en el historial"""
        seleccion = self.tree_historial.selection()
        if seleccion:
            item = self.tree_historial.item(seleccion[0])
            contraseña = item["values"][1]
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(contraseña)
            self.actualizar_barra_estado("Contraseña del historial copiada")
            messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una contraseña del historial")
    
    def limpiar_historial(self):
        """Limpia el historial"""
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea limpiar el historial?"):
            self.historial.clear()
            self.actualizar_tree_historial()
            self.actualizar_barra_estado("Historial limpiado")
    
    def exportar_historial(self):
        """Exporta el historial a un archivo de texto"""
        if not self.historial:
            messagebox.showwarning("Advertencia", "No hay historial para exportar")
            return
        
        try:
            with open("historial_contraseñas.txt", "w", encoding="utf-8") as f:
                f.write("HISTORIAL DE CONTRASEÑAS GENERADAS\n")
                f.write("=" * 50 + "\n\n")
                for item in self.historial:
                    f.write(f"Fecha: {item['fecha']}\n")
                    f.write(f"Contraseña: {item['contraseña']}\n")
                    f.write(f"Longitud: {item['longitud']}\n")
                    f.write(f"Fortaleza: {item['fortaleza']}\n")
                    f.write("-" * 30 + "\n")
            
            self.actualizar_barra_estado("Historial exportado a 'historial_contraseñas.txt'")
            messagebox.showinfo("Éxito", "Historial exportado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar el historial: {str(e)}")
    
    def actualizar_barra_estado(self, mensaje):
        """Actualiza la barra de estado"""
        self.barra_estado.configure(text=mensaje)
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.ventana.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    print("Iniciando Generador de Contraseñas Avanzado...")
    app = GeneradorContraseñasMejorado()
    app.ejecutar()