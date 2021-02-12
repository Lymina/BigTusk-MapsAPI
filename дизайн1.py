<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>617</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="btn_ok">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>40</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>11</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>начать поиск</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="inp_cords">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>70</y>
      <width>291</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>120</y>
      <width>221</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>10</y>
      <width>391</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Введите координаты и выбирите масштаб</string>
    </property>
   </widget>
   <widget class="QLabel" name="image">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>190</y>
      <width>561</width>
      <height>291</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
