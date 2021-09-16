Attribute VB_Name = "Start"
Sub Start()

' clearAll Macro
'
    Cells.Select
    Range("E12").Activate
    Selection.ClearContents
    Range("G16").Select

    
    Dim numType As Integer      'An integer variable to store the total number of types of trucks
    Dim numwarehouse As Integer 'An integer variable to store the total number of warehouses
  
  'Ask user to enter how many type of truck is available
    numType = InputBox(Prompt:="The number of types of trucks you have in depot now is :", _
          Title:="ENTER NUMBER OF TYPES", Default:="The number of types of truck you have in depot now")
    
    'Ask user to enter total number of warehouses
    numwarehouse = InputBox(Prompt:="How many of warehouses are there ", _
          Title:="ENTER NUMBER OF WAREHOUSES", Default:="The number of warehouses here")
          
    'Initiating the format of the worksheet,put in some titles
    Cells(1, 1) = "Data"
    Cells(3, 1) = "Trucks"
    Cells(4, 1) = "Capacity"
    Cells(11, 1) = "Warehouse"
    Cells(10, 2) = "Units"
    Cells(11, 2) = "Available"
         
    Dim i, j As Integer
    
    For i = 1 To numType      'Create a list of subscripts(1,2,3....i) refering to each type of truck
        Cells(2, i + 1) = i
    Next i
    
    For j = 1 To numwarehouse  'Create a list of subscripts(1,2,3...j) refering to each warehouse
        Cells(11 + j, 1) = j
    Next j
 MsgBox "Please fill in all the blanks according to the format generated Then click Continue"
   
End Sub
