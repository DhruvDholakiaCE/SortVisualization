from tkinter import *
import threading
import time
import colors

root = Tk()
# root.resizable(width = False, height= False)
root.title('Sort Visualization')

frame1 = Frame(root, height = 300, width = 500, bg = "white")
frame1.grid(row = 1, columnspan = 50, padx = 10, pady = 10)


nums = [x for x in range(70, 0 ,-1)]
cls = colors.COLORS[23: 23 + len(nums):]

lblList = []


def setIt():

    global lblList
    global nums


    
    if len(lblList) > 0:
        for x in lblList:
            x.destroy()
        lblList =[]


    for i in range(len(nums)):
        lbl = Label(frame1, text = nums[i],  font  =" times 8 bold", bg = cls[i], height = nums[i], width = 3, relief= "flat")
        lbl.grid(column = i , row = 0, pady = 5, sticky = 's')

        lblList.append(lbl)

def Bubble():

    global lblList
    Title['text'] = 'Bubble Sort'
    for i in range(len(lblList)):
        for j in range(len(lblList)):
            if int(lblList[i]['text']) < int(lblList[j]['text']):

                lblList[i]['text'], lblList[j]['text'] = lblList[j]['text'], lblList[i]['text']
                lblList[i]['bg'], lblList[j]['bg'] = lblList[j]['bg'], lblList[i]['bg']
                lblList[i]['height'], lblList[j]['height'] = lblList[j]['height'], lblList[i]['height']

        time.sleep(0.1)

def Insertion():

    global lblList
    Title['text'] = 'Insertion Sort'

    for i in range(1, len(lblList)):
        temp = int(lblList[i]['text'])
        j = i-1
        while j>= 0 and temp< int(lblList[j]['text']):

            lblList[j+1]['text'], lblList[j+1]['bg'], lblList[j+1]['height'], \
                lblList[j]['text'], lblList[j]['bg'], lblList[j]['height'] = \
                    lblList[j]['text'], lblList[j]['bg'], lblList[j]['height'], \
                        lblList[j+1]['text'], lblList[j+1]['bg'], lblList[j+1]['height']

            j -=1
            time.sleep(0.03)
        lblList[j+1]['text'] = str(temp)

def Selection():

    global lblList
    Title['text'] = 'Selection Sort'

    for i in range(0, len(lblList)):
        min = i
        for j in range(i+1, len(lblList)):
            if int(lblList[min]['text']) > int(lblList[j]['text']):
                min = j

        lblList[i]['text'], lblList[i]['bg'], lblList[i]['height'], \
        lblList[min]['text'], lblList[min]['bg'], lblList[min]['height'] = \
            lblList[min]['text'], lblList[min]['bg'], lblList[min]['height'], \
            lblList[i]['text'], lblList[i]['bg'], lblList[i]['height']
        time.sleep(0.1)

# def leftPart(left, A):
#     for i in range(len(A)):
#         A[i].grid(column = i)
#
#
# def rightPart(left,right, A):
#     for j in range(left, right):
#         A[j].grid(column = j)

global cnter
def Merge(left, right, A):

    i = j = k = 0
    while i< len(left) and j< len(right):
        if int(left[i]['text']) < int(right[j]['text']):
            A[k] =  left[i]
            i+=1

        else:

            A[k] = right[j]
            j+=1
        k+=1


    while i<len(left):


        A[k] = left[i]

        i+=1
        k+=1

    while j<len(right):

        A[k] = right[j]

        j+=1
        k+=1

    # threading.Thread(target=lambda :leftPart(i, A)).start()
    # threading.Thread(target=lambda  : rightPart(len(left),len(right), A)).start()






    print(A, '--')
    # for i in range(len(A)):
    #     A[i].grid(column = i)
    #     A[i].grid(column = int(A[i]['text']))
    #     time.sleep(0.1)



def MergeSort(A):
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    if len(A)<2:
        return
    MergeSort(left)
    MergeSort(right)
    Merge(left,right,A)


print(lblList)


setIt()



bubbleTread = threading.Thread(target = Bubble)
insertionThread =  threading.Thread(target = Insertion)
selectionThread = threading.Thread(target = Selection)
mergeThread = threading.Thread(target = lambda : MergeSort(lblList))

Title = Label(root, text = '', font = "times 25 bold")
Title.grid(row = 0, column = 15, ipadx= 100 , pady = 10)

bubble = Button(root, text = 'Bubble Sort' , command = bubbleTread.start, relief = "groove")
bubble.grid(row = 0 , column = 0, pady = 10)

insertion = Button(root, text = 'Insertion Sort' , command = insertionThread.start, relief = "groove")
insertion.grid(row = 0 , column = 1, pady = 10)

selection = Button(root, text = 'Selection Sort' , command = selectionThread.start, relief = "groove")
selection.grid(row = 0 , column = 2, pady = 10)

mergeSort = Button(root, text = 'Merge Sort' , command = mergeThread.start, relief = "groove")
mergeSort.grid(row = 0 , column = 3, pady = 10)

resetButton = Button(root, text = 'Reset' , command = setIt, relief = "groove")
resetButton.grid(row = 0 , column = 4, pady = 10)



root.mainloop()