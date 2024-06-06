from tkinter import *
from tkinter import colorchooser
import math
from tkinter import simpledialog
from tkinter import messagebox
from turtle import width
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import pickle
from PIL import Image, ImageDraw
import PIL.ImageGrab as ImageGrab
import os



class PaintBrush:
    def __init__(self,width,height,title):
        self.screen=Tk()
        self.screen.title(title)
        self.screen.geometry(str(width)+'x'+str(height))

        self.brush_color='black'
        self.last_x,self.last_y=None,None
        self.shape_id=None
        self.brush_width=5
        self.outline_color=self.brush_color
        self.fill_shape_color= ""
        self.fill_color = None
        self.n_polygon=0

        self.text=""
        self.text_size=0
        self.text_style=False
        self.font_style="Arial"

        #Buttons area
        self.button_area=Frame(self.screen,width=width,height=70,bg="sky blue")
        self.button_area.pack(side=TOP)


        #Create Canvas
        self.canvas=Canvas(self.screen,width=width,height=height,bg="white")
        self.canvas.pack()


        #Clear button
        self.clear_button=Button(self.button_area,text="Clear",bg="red",width=4,height=1,
                                 command=self.clear_canvas)
        self.clear_button.place(x=5,y=5)

        #Text button
        self.text_button=Button(self.button_area,text="Text",bg="skyblue",width=4,height=1,
                                 command=self.on_text_button_pressed)
        self.text_button.place(x=5,y=40)


        #Select color button
        
        # self.color_button=Button(self.button_area,text="C\no\nl\no\nr",width=1,height=6,bg="grey")
        # self.color_button.place(x=400,y=5)

        self.green_button=Button(self.button_area,width=1,height=1,bg="green",
                                 command=self.green_color)
        self.green_button.place(x=420,y=5)

        self.blue_button=Button(self.button_area,width=1,height=1,bg="blue",
                                command=self.blue_color)
        self.blue_button.place(x=440,y=5)

        self.yellow_button=Button(self.button_area,width=1,height=1,bg="yellow",
                                  command=self.yellow_color)
        self.yellow_button.place(x=460,y=5)

        self.red_button=Button(self.button_area,width=1,height=1,bg="red",
                               command=self.red_color)
        self.red_button.place(x=480,y=5)

        self.brown_button=Button(self.button_area,width=1,height=1,bg="brown",
                                 command=self.brown_color)
        self.brown_button.place(x=500,y=5)

        self.cyan_button=Button(self.button_area,width=1,height=1,bg="cyan",
                                command=self.cyan_color)
        self.cyan_button.place(x=520,y=5)

        self.black_button=Button(self.button_area,width=1,height=1,bg="black",
                                 command=self.black_color)
        self.black_button.place(x=540,y=5)

        self.grey_button=Button(self.button_area,width=1,height=1,bg="grey",
                                command=self.grey_color)
        self.grey_button.place(x=560,y=5)

        self.orange_button=Button(self.button_area,width=1,height=1,bg="orange",
                                  command=self.orange_color)
        self.orange_button.place(x=580,y=5)

        self.pink_button=Button(self.button_area,width=1,height=1,bg="pink",
                                command=self.pink_color)
        self.pink_button.place(x=600,y=5)

        self.magneta_button=Button(self.button_area,width=1,height=1,bg="magenta",
                                   command=self.magenta_color)
        self.magneta_button.place(x=620,y=5)

        self.indigo_button=Button(self.button_area,width=1,height=1,bg="#4B4B00",
                                  command=self.indigo_color)
        self.indigo_button.place(x=640,y=5)

        self.select_color_button=Button(self.button_area,width=20,height=1,text="Find More Colors",
                                         command=self.select_color,bg="light green")
        self.select_color_button.place(x=420,y=40)




        #Circle Button
        # self.shapes_button=Button(self.button_area,text="S\nH\nA\nP\nE\nS",width=1,height=6,bg="grey")
        # self.shapes_button.place(x=600,y=5)


        #Line Button
        self.arc_button=Button(self.button_area,text="Line",
                                  command=self.on_lineButton_pressed,width=7,height=1
                                  ,bg="brown")
        self.arc_button.place(x=670,y=5)


        self.circle_button=Button(self.button_area,text="Circle",
                                   command=self.on_circleButton_pressed,width=7,height=1
                                   ,bg="lightblue")
        self.circle_button.place(x=735,y=5)

        #Oval button
        self.oval_button=Button(self.button_area,text="Oval",
                                  command=self.on_ovalButton_pressed,width=7,height=1,
                                  bg="lightblue")
        self.oval_button.place(x=800,y=5)


        #Triangle Button
        self.triangle_button=Button(self.button_area,text="Triangle",
                                  command=self.on_triangleButton_pressed,width=7,height=1,
                                  bg="light pink")
        self.triangle_button.place(x=865,y=5)

         #Right Triangle Button
        self.rightTriangle_button=Button(self.button_area,text="R-Triangle",
                                  command=self.on_rightTriangleButton_pressed,width=7,height=1,
                                  bg="light pink")
        self.rightTriangle_button.place(x=930,y=5)


        #Square Button
        self.square_button=Button(self.button_area,text="Square",
                                  command=self.on_squareButton_pressed,width=7,height=1,
                                  bg="grey")
        #self.icon_image = PhotoImage(file="square.png")
        #self.icon_image = self.icon_image.subsample(2, 2)
        # self.icon_image.width=10
        # self.icon_image.height=10
        #self.square_button.config(image=self.icon_image,compound="left")
        self.square_button.place(x=670,y=40)


        #Rectangle Button
        self.rectangle_button=Button(self.button_area,text="Rectangle",
                                  command=self.on_rectangleButton_pressed,width=7,height=1,
                                  bg="grey")
        self.rectangle_button.place(x=735,y=40)

        
        #Pentagon Button
        self.pentagon_button=Button(self.button_area,text="Pentagon",
                                  command=self.on_pentagonButton_pressed,width=7,height=1,
                                  bg="green")
        self.pentagon_button.place(x=800,y=40)


        #Hexagon Button
        self.hexagon_button=Button(self.button_area,text="Hexagon",
                                  command=self.on_hexagonButton_pressed,width=7,height=1,
                                  bg="green")
        self.hexagon_button.place(x=865,y=40)

       
        #Star Button
        self.star_button=Button(self.button_area,text="Star",
                                  command=self.on_starButton_pressed,width=7,height=1,
                                  bg="yellow")
        self.star_button.place(x=930,y=40)


        #N-Polygon Button
        self.npolygon_button=Button(self.button_area,text="P\no\nl\ny",
                                  command=self.on_npolygonButton_pressed,width=1,height=4,
                                  bg="blue")
        self.npolygon_button.place(x=995,y=2)


        #Beziar Curves
        self.beziar_button=Button(self.button_area,width=10,height=1,text="Beziar",
                                         command=self.on_beziar_button_pressed,bg="light green")
        self.beziar_button.place(x=578,y=40)



        #Eraser button
        self.eraser_button=Button(self.button_area,text="Eraser",
                                 command=self.on_eraserButton_pressed,width=10,height=1)
        self.eraser_button.place(x=100,y=5)


        #Color Eraser button
        self.color_eraser_button=Button(self.button_area,width=10,height=1,text="Color Eraser",
                                         command=self.on_color_eraser_pressed,
                                         bg="purple")
        self.color_eraser_button.place(x=100,y=40)


        #Brush button
        self.brush_button=Button(self.button_area,text="Brush",
                                 command=self.on_brushButton_pressed,width=5,height=1,
                                 bg="grey")
        self.brush_button.place(x=185,y=5)

        #Brush 5 button
        self.brush_button=Button(self.button_area,text="5",
                                 command=self.on_width5_pressed,width=5,height=1,
                                 bg="grey")
        self.brush_button.place(x=235,y=5)

        #Brush 10 button
        self.brush_button=Button(self.button_area,text="10",
                                 command=self.on_width10_pressed,width=5,height=1,
                                 bg="grey")
        self.brush_button.place(x=185,y=40)

        #Brush 15 button
        self.brush_button=Button(self.button_area,text="15",
                                 command=self.on_width15_pressed,width=5,height=1,
                                 bg="grey")
        self.brush_button.place(x=235,y=40)

        #Brush More button
        self.brush_button=Button(self.button_area,text="M\no\nr\ne",
                                 command=self.on_width_more_pressed,width=2,height=4,
                                 bg="grey")
        self.brush_button.place(x=285,y=5)


        #Zoom in button
        self.zoom_in_button=Button(self.button_area,text="Zoom In",
                                 command=self.on_zoom_in_pressed,width=8,height=1,
                                 bg="orange")
        self.zoom_in_button.place(x=1125,y=5)

        #Zoom out button
        self.zoom_out_button=Button(self.button_area,text="Zoom Out",
                                 command=self.on_zoom_out_pressed,width=8,height=1,
                                 bg="orange")
        self.zoom_out_button.place(x=1125,y=40)


        #Bucket fill button
        self.bucket_fill_button=Button(self.button_area,text="Fill\nColor",
                                command=self.on_bucket_fill_pressed,width=5,height=3,bg="light pink")
        self.bucket_fill_button.place(x=315,y=7)

        #Fill Shapes button
        self.fill_shape_button=Button(self.button_area,text="Fill\nShape",
                                command=self.on_fill_shape_pressed,width=5,height=3,
                                bg="yellow green")
        self.fill_shape_button.place(x=365,y=7)


        

        #load button
        self.load_button = Button(self.button_area, text="load", 
                                  command=self.load_canvas
                                  , bg="yellow green",width=5, height=1)
        self.load_button.place(x=50,y=40)
        # save button
        self.save_button = Button(self.button_area, text="Save",
                                 command=self.save_canvas
                                  , bg="yellow green",width=5, height=1)
        self.save_button.place(x=50,y=5)


        #Select button
        self.select_area_button=Button(self.button_area,text="Select\narea",
                                command=self.on_select_area_pressed,width=5,height=3,
                                bg="yellow green")
        self.select_area_button.place(x=1020,y=5)

        #Color picker button
        self.color_picker_button=Button(self.button_area,text="Color\nPicker",
                                command=self.get_color,width=5,height=3,
                                bg="pink")
        self.color_picker_button.place(x=1070,y=5)

       


    


        


        


        


        


        #bind function to the mouse
        self.canvas.bind("<B1-Motion>",self.brush_draw)
        self.canvas.bind("<ButtonRelease-1>",self.brush_draw_end)
        #Bind function for color picker 
        self.canvas.bind("<Button-1>",self.get_color)
        #self.canvas.bind("<Button-1>",self.on_canvas_clck)

        

    def on_fill_shape_pressed(self):
        selected_color=colorchooser.askcolor()
        if selected_color[1]==None:
            return
        self.fill_shape_color=selected_color[1]
        #self.outline_color=self.brush_color

    def on_circleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_circle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_circle_end)
    def draw_circle(self,event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x,self.last_y=event.x,event.y
            return
        radius = abs(self.last_x - event.x )+abs(self.last_y-event.y)
        x1,y1=(self.last_x-radius),(self.last_y-radius)
        x2,y2=(self.last_x+radius),(self.last_y+radius)
        self.shape_id=self.canvas.create_oval(x1,y1,x2,y2,outline =self.outline_color,fill=self.fill_shape_color,width=self.brush_width)#,fill=self.brush_color,outline='black')
    def draw_circle_end(self,event):
        self.last_x,self.last_y=None,None
        self.shape_id=None


    def on_ovalButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_oval)
        self.canvas.bind("<ButtonRelease-1>",self.draw_oval_end)
    def draw_oval(self,event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        radius_x = abs(self.last_x - event.x)
        radius_y = abs(self.last_y - event.y)
        x1, y1 = self.last_x - radius_x, self.last_y - radius_y
        x2, y2 = self.last_x + radius_x, self.last_y + radius_y
        self.shape_id = self.canvas.create_oval(x1, y1, x2, y2, outline=self.outline_color,fill=self.fill_shape_color,width=self.brush_width)#,fill=self.brush_color,outline='black')
    def draw_oval_end(self,event):
        self.last_x,self.last_y=None,None
        self.shape_id=None
        

    def on_rectangleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_rectangle_end)
    def draw_rectangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        self.shape_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.outline_color,fill=self.fill_shape_color,width=self.brush_width)
    def draw_rectangle_end(self,event):
        self.last_x,self.last_y=None,None
        self.shape_id=None


    def on_squareButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_square)
        self.canvas.bind("<ButtonRelease-1>",self.draw_square_end)
    def draw_square(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        size = min(abs(x2 - x1), abs(y2 - y1))
        if x2 < x1:
            x1 = x1 - size  
        if y2 < y1:
            y1 = y1 - size  
        self.shape_id = self.canvas.create_rectangle(x1, y1, x1 + size, y1 + size, outline=self.outline_color,fill=self.fill_shape_color,width=self.brush_width)
    def draw_square_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None


    def on_rightTriangleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_rightTriangle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_rightTriangle_end)
    def draw_rightTriangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        x3, y3 = x1, y2  
        triangle_coords = [x1, y1, x2, y2, x3, y3]
        self.shape_id = self.canvas.create_polygon(triangle_coords,fill=self.fill_shape_color, outline=self.outline_color,width=self.brush_width)
    def draw_rightTriangle_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None


    def on_triangleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_triangle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_triangle_end)
    def draw_triangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        cx = (self.last_x+event.x)//2
        cy = (self.last_y+event.y)//2
        
        x3, y3 = cx-(y2-cy), cy+(x2-cx)  
        triangle_coords = [x1, y1, x2, y2, x3, y3, x1, y1]
        self.shape_id = self.canvas.create_polygon(triangle_coords,fill=self.fill_shape_color, outline=self.outline_color,width=self.brush_width)
    def draw_triangle_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None


    # def rotate_point(x, y, cx, cy, angle):
    #     # Rotate the point (x, y) around the center (cx, cy) by the given angle (in degrees)
    #     theta = math.radians(angle)
    #     cos = math.cos(theta)
    #     sin = math.sin(theta)
    #     nx = cos * (x - cx) - sin * (y - cy) + cx
    #     ny = sin * (x - cx) + cos * (y - cy) + cy
    #     return nx, ny
    def on_pentagonButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_pentagon)
        self.canvas.bind("<ButtonRelease-1>",self.draw_pentagon_end)
    def draw_pentagon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        cx = (self.last_x + event.x) // 2
        cy = (self.last_y + event.y) // 2

        angle = 360 / 5  # Angle between each vertex of the pentagon

        pentagon_coords = []
        for i in range(5):
            theta = math.radians(i * angle)
            px = cx + math.cos(theta) * (x2 - cx) - math.sin(theta) * (y2 - cy)
            py = cy + math.sin(theta) * (x2 - cx) + math.cos(theta) * (y2 - cy)
            pentagon_coords.extend([px, py])

        self.shape_id =  self.canvas.create_polygon(pentagon_coords, fill=self.fill_shape_color, outline=self.outline_color,width=self.brush_width)
    def draw_pentagon_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None
    

    def on_hexagonButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_hexagon)
        self.canvas.bind("<ButtonRelease-1>",self.draw_hexagon_end)
    def draw_hexagon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        cx = (self.last_x + event.x) // 2
        cy = (self.last_y + event.y) // 2

        angle = 360 / 6  # Angle between each vertex of the pentagon

        pentagon_coords = []
        for i in range(6):
            theta = math.radians(i * angle)
            px = cx + math.cos(theta) * (x2 - cx) - math.sin(theta) * (y2 - cy)
            py = cy + math.sin(theta) * (x2 - cx) + math.cos(theta) * (y2 - cy)
            pentagon_coords.extend([px, py])

        self.shape_id =  self.canvas.create_polygon(pentagon_coords, fill=self.fill_shape_color, outline=self.outline_color,width=self.brush_width)
    def draw_hexagon_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None
    

    def on_starButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.draw_star)
        self.canvas.bind("<ButtonRelease-1>",self.draw_star_end)
    def draw_star(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        outer_radius = abs(x2 - cx)
        inner_radius = outer_radius // 2

        num_points = 5
        angle = (2 * math.pi) / num_points

        star_coords = []
        for i in range(num_points):
            outer_theta = i * angle - math.pi / 2  # Subtract math.pi / 2 to start from the top
            inner_theta = outer_theta + angle / 2

            outer_px = cx + math.cos(outer_theta) * outer_radius
            outer_py = cy + math.sin(outer_theta) * outer_radius

            inner_px = cx + math.cos(inner_theta) * inner_radius
            inner_py = cy + math.sin(inner_theta) * inner_radius

            star_coords.extend([outer_px, outer_py, inner_px, inner_py])

        self.shape_id = self.canvas.create_polygon(star_coords, smooth=True, fill=self.fill_shape_color, outline=self.outline_color, width=self.brush_width)
    def draw_star_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None
    

    def on_npolygonButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        n = simpledialog.askinteger("Polygon", "Enter the number of sides:")
        self.n_polygon=n
        self.canvas.bind("<B1-Motion>",self.draw_npolygon)
        self.canvas.bind("<ButtonRelease-1>",self.draw_npolygon_end)
    def draw_npolygon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        # Obtain the number of sides from a dialog box
        # n = simpledialog.askinteger("Polygon", "Enter the number of sides:")
        if self.n_polygon is None or self.n_polygon < 3:
            return
        # Obtain the distance of the polygon from a dialog box
        #distance = simpledialog.askfloat("Polygon", "Enter the distance of the polygon:")
        #if distance is None or distance <= 0:
         #   return
        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        cx = (self.last_x + event.x) // 2
        cy = (self.last_y + event.y) // 2

        angle = 360 / self.n_polygon  # Angle between each vertex of the pentagon

        pentagon_coords = []
        for i in range(self.n_polygon):
            theta = math.radians(i * angle)
            px = cx + math.cos(theta) * (x2 - cx) - math.sin(theta) * (y2 - cy)
            py = cy + math.sin(theta) * (x2 - cx) + math.cos(theta) * (y2 - cy)
            pentagon_coords.extend([px, py])

        self.shape_id =  self.canvas.create_polygon(pentagon_coords, fill=self.fill_shape_color, outline=self.outline_color,width=self.brush_width)
    def draw_npolygon_end(self, event):
        self.last_x, self.last_y = None,None
        self.shape_id = None
        
    
    def on_beziar_button_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>", self.bezier_draw)
        self.canvas.bind("<ButtonRelease-1>", self.bezier_draw_end)
    def draw_bezier_segments(canvas, points, color, width):
        # Draw line segments connecting the points
        segment_ids = []
        for i in range(len(points) - 2):
            x1, y1 = points[i], points[i + 1]
            x2, y2 = points[i + 2], points[i + 3]
            segment_id = canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
            segment_ids.append(segment_id)
        return segment_ids
    def bezier_draw(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        
        control_x1 = self.last_x
        control_y1 = self.last_y
        control_x2 = event.x
        control_y2 = event.y

        # Calculate intermediate points along the Bezier curve
        num_segments = 100
        points = []
        for i in range(num_segments + 1):
            t = i / num_segments
            x = int(
                (1 - t) ** 3 * self.last_x
                + 3 * (1 - t) ** 2 * t * control_x1
                + 3 * (1 - t) * t ** 2 * control_x2
                + t ** 3 * event.x
            )
            y = int(
                (1 - t) ** 3 * self.last_y
                + 3 * (1 - t) ** 2 * t * control_y1
                + 3 * (1 - t) * t ** 2 * control_y2
                + t ** 3 * event.y
            )
            points.append(x)
            points.append(y)

        # Draw the Bezier curve using line segments
        self.shape_id = draw_bezier_segments(self.canvas, points, self.brush_color, self.brush_width)
    def bezier_draw_end(self, event):
        self.last_x, self.last_y = None, None
        self.shape_id = None
    


    def on_lineButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.line_draw)
        self.canvas.bind("<ButtonRelease-1>",self.line_draw_end)
    def line_draw(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        self.shape_id=self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.brush_color, width=self.brush_width)
    def line_draw_end(self,event):
        self.last_x,self.last_y=None,None
        self.shape_id=None


    def green_color(self):
        self.brush_color= 'green'
        self.outline_color=self.brush_color
    def blue_color(self):
        self.brush_color= 'blue'
        self.outline_color=self.brush_color
    def yellow_color(self):
        self.brush_color= 'yellow'
        self.outline_color=self.brush_color
    def red_color(self):
        self.brush_color= 'red'
        self.outline_color=self.brush_color
    def brown_color(self):
        self.brush_color= 'brown'
        self.outline_color=self.brush_color
    def cyan_color(self):
        self.brush_color= 'cyan'
        self.outline_color=self.brush_color
    def black_color(self):
        self.brush_color= 'black'
        self.outline_color=self.brush_color
    def grey_color(self):
        self.brush_color= 'grey'
        self.outline_color=self.brush_color
    def orange_color(self):
        self.brush_color= 'orange'
        self.outline_color=self.brush_color
    def pink_color(self):
        self.brush_color= 'pink'
        self.outline_color=self.brush_color
    def magenta_color(self):
        self.brush_color= 'magenta'
        self.outline_color=self.brush_color
    def indigo_color(self):
        self.brush_color= 'indigo'
        self.outline_color=self.brush_color
    def select_color(self):
        selected_color=colorchooser.askcolor()
        if selected_color[1]==None:
            return
        self.brush_color=selected_color[1]
        self.outline_color=self.brush_color


    def clear_canvas(self):
        self.canvas.delete("all")
    
    def on_text_button_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        text = simpledialog.askstring("Text Input", "Enter your text:")
        self.text=text
        font_style = simpledialog.askstring("Font Style", "Enter style of your text:")
        self.font_style=font_style
        text_size = simpledialog.askinteger("Text Size", "Enter your text size:")
        self.text_size=text_size
        text_style = simpledialog.askstring("Bold", "Bold (y/n)?")
        if text_style == "y":
            self.text_style=True
        else:
            self.text_style=False

        self.canvas.bind("<B1-Motion>",self.create_text)
        self.canvas.bind("<ButtonRelease-1>",self.create_text_end)
    def create_text(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        if self.text:
            if self.text_style is True:
                self.shape_id=self.canvas.create_text(event.x, event.y, text=self.text, font=(self.font_style, self.text_size, "bold"), fill=self.fill_color)
            else:
                self.shape_id=self.canvas.create_text(event.x, event.y, text=self.text, font=(self.font_style, self.text_size), fill=self.fill_color)
    def create_text_end(self, event):
        self.last_x,self.last_y=None,None
        self.shape_id=None


    def on_eraserButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.eraser_canvas)
        self.canvas.bind("<ButtonRelease-1>", self.eraser_end)
        #self.set_eraser_cursor()

    def eraser_canvas(self, event):
        if self.last_x==None:
            self.last_x,self.last_y=event.x,event.y
            return
        # Get the current mouse position
        x = event.x
        y = event.y

        # Define the eraser size
        eraser_size = self.brush_width

        # Create a rectangle with the eraser size centered at the mouse position
        x1 = x - eraser_size // 2
        y1 = y - eraser_size // 2
        x2 = x + eraser_size // 2
        y2 = y + eraser_size // 2

        # Erase the area by filling it with the canvas background color
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.canvas['bg'], outline='')
        self.last_x,self.last_y=event.x,event.y
    def eraser_end(self, event):
        self.last_x,self.last_y=None,None

    # def color_eraser_canvas(self):
    #     selected_color=colorchooser.askcolor()
    #     if selected_color[1]==None:
    #         return
    #     self.brush_color=selected_color[1]
    #     self.outline_color=self.brush_color
    def on_color_eraser_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        selected_color=colorchooser.askcolor()
        if selected_color[1]==None:
            return
        self.brush_color=selected_color[1]
        self.canvas.bind("<B1-Motion>",self.color_eraser_canvas)
        self.canvas.bind("<ButtonRelease-1>",self.color_eraser_end)
    def color_eraser_canvas(self,event):
        if self.last_x==None:
            self.last_x,self.last_y=event.x,event.y
            return
        # Get the current mouse position
        x = event.x
        y = event.y
        # Define the eraser size
        eraser_size = self.brush_width
        # Create a rectangle with the eraser size centered at the mouse position
        x1 = x - eraser_size // 2
        y1 = y - eraser_size // 2
        x2 = x + eraser_size // 2
        y2 = y + eraser_size // 2
        # Erase the area by filling it with the canvas background color
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.brush_color, outline='')
        self.last_x,self.last_y=event.x,event.y
    def color_eraser_end(self,event):
        self.last_x,self.last_y=None,None
    

    def on_width5_pressed(self):
        self.brush_width=5
    def on_width10_pressed(self):
        self.brush_width=10
    def on_width15_pressed(self):
        self.brush_width=15
    def on_width_more_pressed(self):
        # Obtain the width from a dialog box
        n = simpledialog.askinteger("Width", "Enter the Size of Brush:")
        self.brush_width=n
        

    def on_zoom_in_pressed(self):
        self.canvas.scale("all", self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, 1.1, 1.1)
    def on_zoom_out_pressed(self):
        self.canvas.scale("all", self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, 0.9, 0.9)
   

    def on_bucket_fill_pressed(self):
        color = colorchooser.askcolor(title="Color for fill")
        if color:
            self.fill_color = color[1]
            self.canvas.bind("<Button-1>", self.on_canvas_click)  # Add binding to the canvas click event
        else:
            self.brush_color = color
            #self.canvas.unbind("<Button-1>")
    def on_canvas_click(self,event):
        shape_id=self.canvas.find_closest(event.x,event.y)
        self.fill_area(shape_id)
        self.canvas.unbind("<Button-1>")
    def fill_area(self,shape_id):
        self.canvas.itemconfig(shape_id,fill=self.fill_color)
    
    

    
    def sav_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if file_path:
            ImageGrab.grab().save(file_path)
    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if file_path:
            # Calculate the bounding box of the canvas
            x = self.canvas.winfo_rootx() + self.canvas.winfo_x()
            y = self.canvas.winfo_rooty() + self.canvas.winfo_y()
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()

            # Take a screenshot of the canvas area only
            image = ImageGrab.grab(bbox=(x+40, y+25, x + width, y + height))
            #resized_image = image.resize((width // 5, height // 5))
            # Set the DPI value to match the screen's DPI
            image.save(file_path)

    def load_canvas(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif"
                                                        "*.PNG;*.JPG;*.JPEG;*.GIF")])
        if file_path:
            # Delete existing items on the canvas
            self.canvas.delete("all")

            # Load the image
            image = Image.open(file_path)

            # Calculate the aspect ratio of the image
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image_width, image_height = image.size
            aspect_ratio = min(canvas_width / image_width, canvas_height / image_height)

            # Resize the image while maintaining its aspect ratio
            new_width = int(image_width * aspect_ratio)
            new_height = int(image_height * aspect_ratio)
            image = image.resize((new_width, new_height), Image.ANTIALIAS)

            # Create a blank white background image of canvas size
            background_image = Image.new("RGB", (canvas_width, canvas_height), "white")

            # Calculate the position to center the resized image on the background
            x = (canvas_width - new_width) // 2
            y = (canvas_height - new_height) // 2

            # Paste the resized image onto the background
            background_image.paste(image, (x, y))

            # Create a PhotoImage object from the background image
            photo = ImageTk.PhotoImage(background_image)

            # Create an image item on the canvas
            self.canvas.create_image(0, 0, anchor="nw", image=photo)
            self.canvas.image = photo


    def lod_canvas(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif"
                                                          "*.PNG;*.JPG;*.JPEG;*.GIF")])
        if filename:
            # Clear the canvas
            self.canvas.delete("all")
            
            # Load the image onto the canvas
            self.image = PhotoImage(file=filename)
            self.canvas.create_image(0, 0, image=self.image, anchor=NW)
            self.canvas.image = self.image 
            self.canvas.update()

    def on_load_button_pressed(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.PNG;*.JPG;*.JPEG;*.GIF")])
        if filename:
            # Clear the canvas
            self.canvas.delete("all")

            # try:
            #     # Load the image onto the canvas
            #     self.image = ImageTk.PhotoImage(file=filename)
            #     self.canvas.create_image(0, 0, image=self.image, anchor=NW)
            #     self.canvas.image = self.image
            #     self.canvas.update()
            # except Exception as e:
                # Display an error message if the image cannot be loaded
                #messagebox.showerror("Error", f"Failed to load image: {e}")


   
    def on_select_area_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonPress-1>",self.sel_area_press)
        self.canvas.bind("<B1-Motion>",self.sel_area_move)
        self.canvas.bind("<ButtonRelease-1>",self.sel_area_release)
    def sel_area_press(self,event):
        self.sel_start=(event.x,event.y)
    def sel_area_move(self,event):
        if self.sel_start is not None:
            self.sel_end=(event.x,event.y)
            self.update_sel_area()
    def sel_area_release(self,event):
        if self.sel_start is not None:
            self.sel_end=(event.x,event.y)
            self.update_sel_area()
    def update_sel_area(self):
        self.canvas.delete("selected_part")
        if self.sel_start is not None and self.sel_end is not None:
            x1,y1=self.sel_start
            x2,y2=self.sel_end
            self.canvas.create_rectangle(x1,y1,x2,y2,outline=self.outline_color,width=self.brush_width,tags="selected_part")
    
    
    def sel_col_but(self,col):
        self.brush_color=col
    def select_col(self):
        selected_color=colorchooser.askcolor()
        if selected_color[1] is not None:
            self.brush_color=selected_color[1]
    def pick_color(self):
        color=colorchooser.askcolor(title="pick a color")
        if color:
            self.canvas.config(bg=color[1])
    def get_color(self,event):
        x=event.x
        y=event.y
        items=self.canvas.find_closest(x,y)
        if items:
            item=items[-1]
            color =self.canvas.itemcget(item,"fill")
            print("Selected color:",color)

    def run(self):
        self.screen.mainloop()

 
    def on_brushButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind("<B1-Motion>",self.brush_draw)
        self.canvas.bind("<ButtonRelease-1>",self.brush_draw_end)
    def brush_draw(self,event):
        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,
                                width=self.brush_width,capstyle=ROUND,fill=self.brush_color)
        self.last_x,self.last_y=event.x,event.y
    def brush_draw_end(self,event):
        self.last_x,self.last_y=None,None




PaintBrush(1200,600,"Bscs22017").run()

