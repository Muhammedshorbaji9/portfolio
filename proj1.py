from tkinter import *
from tkinter import ttk
import pymysql

class Student:
#sekme olusturma - انشاء نافذة
        def __init__(self,root):
                self.root = root
                self.root.geometry('1350x690+40+40')
                self.root.title('Okul yonetim sistemi')
                self.root.configure(background='#9999cc')
                self.root.resizable(False,False)#False anlami: genislenmez , False anlami: kontrol edilemez demek
                title = Label(self.root,
                        text='ÖĞRENCİ KAYIT SİSTEMİ',background='#6666ff',fg='white',font=('monospace',10,'bold'))#master : bu label'in nerede gozukeceği ,,, optıon : bu labelın ozellıklerı
                title.pack(fill=X)

                #-----------------------------------------variable - değişkenler--------------------------------------------------------------
                self.id_var=StringVar()
                self.name_var=StringVar()
                self.email_var=StringVar()
                self.phone_var=StringVar()
                self.moahel_var=StringVar()
                self.gender_var=StringVar()
                self.address_var=StringVar()
                self.dele_var=StringVar()
                self.se_var=StringVar()
                self.se_by=StringVar()



                Manag_Frame=Frame(self.root,bg="white")
                Manag_Frame.place(x=1138,y=23,width=210,height=400)

                lbl_id=Label(Manag_Frame,text='Öğrenci Numarasi',fg='#6666ff',bg='white')
                lbl_id.pack()
                id_entry=Entry(Manag_Frame,textvariable=self.id_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                id_entry.pack()

                lbl_name=Label(Manag_Frame,text='Öğrenci adı',bg='white',fg='#6666ff')
                lbl_name.pack()
                name_entry=Entry(Manag_Frame,textvariable=self.name_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                name_entry.pack()

                lbl_email=Label(Manag_Frame,text='E-mail',bg='white',fg='#6666ff')
                lbl_email.pack()
                email_entry=Entry(Manag_Frame,textvariable=self.email_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                email_entry.pack()

                lbl_phone=Label(Manag_Frame,text='Telefon Numarası',bg='white',fg='#6666ff')
                lbl_phone.pack()
                phone_entry=Entry(Manag_Frame,textvariable=self.phone_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                phone_entry.pack()

                lbl_certi=Label(Manag_Frame,text='Sertifikalar',bg='white',fg='#6666ff')
                lbl_certi.pack()
                certi_entry=Entry(Manag_Frame,textvariable=self.moahel_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                certi_entry.pack()

                lbl_gender=Label(Manag_Frame,text='Cinsiyet',bg='white',fg='#6666ff')
                lbl_gender.pack()
                combo_gender=ttk.Combobox(Manag_Frame,textvariable=self.gender_var)
                combo_gender['value']=('Erkek','Kadin')
                combo_gender.pack()

                lbl_address=Label(Manag_Frame,text='Adres Bilgisi',bg='white',fg='#6666ff')
                lbl_address.pack()
                address_entry=Entry(Manag_Frame,textvariable=self.address_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                address_entry.pack()

                lbl_delete=Label(Manag_Frame,text='Kayıt Sil',bg='white',fg='red',font=('Bold',11))
                lbl_delete.pack()
                delete_entry=Entry(Manag_Frame,textvariable=self.dele_var,bd=4,justify=CENTER)# bd : border demek///justify : ortadan yada sagdan ya da soldan yazmak icin
                delete_entry.pack()
        #-----------------------BUTTONS الازرار--------------------------------------------------------------------------------------------------
                btn_frame=Frame(self.root,bg='white')
                btn_frame.place(x=1137,y=425,width=210,height=259)
                title_lbl=Label(btn_frame, text='CONTROL PANEL',font=('bold',12),fg='white',bg='#6666ff')
                title_lbl.pack(fill=X)


                add_btn=Button(btn_frame,text='Öğrenci Ekle',bg='#AED6F1',command=self.add_Student)
                add_btn.place(x=33,y=25,width=150,height=30)
                
                delete_btn=Button(btn_frame,text='Öğrenci Sil',bg='#AED6F1',command=self.delete)
                delete_btn.place(x=33,y=61,width=150,height=30)

                update_btn=Button(btn_frame,text='Öğrenci Güncelle',background='#AED6F1',command=self.update )
                update_btn.place(x=33,y=101,width=150,height=30)

                clear_btn=Button(btn_frame,text='Temizle',bg='#AED6F1', command=self.clear)
                clear_btn.place(x=33,y=141,width=150,height=30)

                about_btn=Button(btn_frame,text='Hakkımızda',bg='#AED6F1')
                about_btn.place(x=33,y=181,width=150,height=30)

                exit_btn=Button(btn_frame,text='Uygulamayı Kapat',bg='red',command=self.kapat)
                exit_btn.place(x=33,y=221,width=150,height=30)

        #-------------------------------SEARCH - ARAMA ------------------------------
                search_frame=Frame(self.root,bg='white')
                search_frame.place(x=1,y=24,width=1135,height=50)

                lbl_search=Label(search_frame,text='Kayıt Arama',bg='white')
                lbl_search.place(x=1061,y=12)

                combo_search = ttk.Combobox(search_frame,justify='left')
                combo_search['value']=('Kayıt No','Ad','E-mail','Telefon')
                combo_search.place(x=910,y=12)

                search_entry =Entry(search_frame,textvariable=self.se_var,justify='center',bd=4)
                search_entry.place(x=770,y=12)

                search_btn=Button(search_frame,text='Ara',bg='#6666ff',fg='white')
                search_btn.place(x=650,y=12,width=110,height=23)
                #----------------------------------------------sonuclari gosterme - عرض النتائج----------------------------------------------------------------
                dietals_frame=Frame(self.root,bg='#6666ff')
                dietals_frame.place(x=1,y=76,width=1135,height=609)
                #------------------------------------------------------SCROLLBARS--------------------------------------------------------------------------
                scroll_x=Scrollbar(dietals_frame,orient=HORIZONTAL)
                scroll_y=Scrollbar(dietals_frame,orient=HORIZONTAL)
                #------------------------------------------------------tree view--------------------------------------------------------------------------
                self.student_table=ttk.Treeview(
                columns=('id','name','email','phone','certi','gender','address'),
                xscrollcommand=scroll_x.set,
                yscrollcommand=scroll_y.set)
                self.student_table.place(x=17,y=75,width=1118,height=592)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=LEFT,fill=Y)

                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)
                self.student_table['show']='headings'
                self.student_table.heading('address',text='Adres Bilgisi')
                self.student_table.heading('gender',text='Cinsiyet')
                self.student_table.heading('certi',text='Sertifikalar')
                self.student_table.heading('phone',text='Telefon Numarası')
                self.student_table.heading('email',text='E-mail')
                self.student_table.heading('name',text='Öğrenci Adı')
                self.student_table.heading('id',text='ID')
                #------------------------------------------------------التحكم بعرض الحقول--------------------------------------------------------------------------
                self.student_table.column('id',width=50)
                self.student_table.column('name',width=150)
                self.student_table.column('email',width=130)
                self.student_table.column('phone',width=130)
                self.student_table.column('certi',width=130)
                self.student_table.column('gender',width=80)
                self.student_table.column('id',width=50)
                self.student_table.bind("<ButtonRelease-1>",self.get_cursor)#حدث النقر بالفارة -يتم التنفيذ

#---------------veri tabanla baglanma -------------------------------------------------------------------------------------------------------------------------


                self.fetch_all() #verileri STUDENT_TABLE'DE GOSTERMEK ICIN KULLANILIR
        def add_Student(self):
                con=pymysql.connect(host='localhost',user='root',password='',database='stud')
                cur=con.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.id_var.get(),
                                                        self.name_var.get(),
                                                        self.email_var.get(),
                                                        self.phone_var.get(),
                                                        self.moahel_var.get(),
                                                        self.gender_var.get(),
                                                        self.address_var.get()
                                                               ))
                
#--------------------------------verileri student_table'de gosterme-----------------------------------------------------------------------
             
                con.commit()
                self.fetch_all()
                self.clear()
                con.close()
 #--------------------------------verileri student_table'de gosterme-----------------------------------------------------------------------
        
        def fetch_all(self):
                con = pymysql.connect(host="localhost", user="root",password="",database="stud")#الاتصال بقاعدة البيانات
                cur = con.cursor()
                cur.execute("select * from student")# ' * ' all ya da her sey demek
                rows = cur.fetchall()
                if len (rows) != 0:
                        self.student_table.delete(*self.student_table.get_children())
                        for row in rows:
                                self.student_table.insert("",END,value=row) # 'END' GOREVİ : ID'yi sıralama
                        con.commit()  
                con.close()    
 #----------------------------------------silme islemi---------------------------------------------------------------

        def delete(self):
                con = pymysql.connect(host="localhost", user="root",password="",database="stud")
                cur = con.cursor()
                cur.execute('delete from student where name=%s',self.dele_var.get())#تنفيذ المطلوب ضمن الاقواس
                cur.execute('delete from student where id=%s',self.dele_var.get())#تنفيذ المطلوب ضمن الاقواس

                con.commit()
                self.fetch_all()
                con.close()
 #----------------------------------------temizleme islemi---------------------------------------------------------------
        def clear(self):
                self.id_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه----------set : koy demektir // get : getir demektir
                self.name_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه
                self.email_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه
                self.phone_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه
                self.moahel_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه
                self.gender_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه
                self.address_var.set('')#عندما يكون هذا الحقل فيه كتابة فم بافراغه
        def kapat(self):
                root.destroy()
 #----------------------------------------bilgileri yerine getirme islemi---------------------------------------------------------------
        def get_cursor(self,muhammet):
                cursor_row=self.student_table.focus()
                contents=self.student_table.item(cursor_row)
                row=contents['values']
                self.id_var.set(row[0])
                self.name_var.set(row[1])
                self.email_var.set(row[2])
                self.phone_var.set(row[3])
                self.moahel_var.set(row[4])
                self.gender_var.set(row[5])
                self.address_var.set(row[6])
                #----------------------------------------update---------------------------------------------------------------
        def update(self):
                con=pymysql.connect(host='localhost',user='root',password='',database='stud')
                cur=con.cursor()
                cur.execute("update student set address=%s, gender=%s, moahel=%s, email=%s, phone=%s, name=%s where id=%s",(
                                                        
                                                        self.address_var.get(),
                                                        self.gender_var.get(),
                                                        self.moahel_var.get(),
                                                        self.phone_var.get(),
                                                        self.email_var.get(),
                                                        self.name_var.get(),
                                                        self.id_var.get()
                                                        
                                                        
                                                               ))
                
#--------------------------------verileri student_table'de gosterme-----------------------------------------------------------------------
             
                con.commit()
                self.fetch_all()
                self.clear()
                con.close()

        




                
                


root = Tk()
ob = Student(root)
root.mainloop()