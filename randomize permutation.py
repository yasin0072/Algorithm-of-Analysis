import random
import matplotlib.pyplot as plt
global total_Times_row_Repeated, no_of_comparisons, no_of_exchangers
total_Times_row_Repeated, no_of_comparisons, no_of_exchangers = 0,0,0


def randomize(arr):
    for j in range(len(arr) - 1, 0, -1):
        temp = random.randint(0, j - 1)
        arr[j], arr[temp] = arr[temp], arr[j]
    return arr


def hiring(arr1):
    hired = 0
    best = 0
    for i in range(0, len(arr1)):
        if arr1[i] > best:
            hired += 1
            best = arr1[i]
    return hired


def insertionSort(arr1):
  total_Times_row_Repeated =0
  no_of_exchangers=0
  no_of_comparisons=0

  for i in range(1, len(arr1)):
      # no_of_comparisons += 1
      key = arr1[i]
      j = i - 1
      total_Times_row_Repeated += 3
      while j >= 0 and key < arr1[j]:
        no_of_comparisons+=1
        arr1[j + 1] = arr1[j]
        no_of_exchangers+=1
        j -= 1
        total_Times_row_Repeated+=3
      total_Times_row_Repeated +=2
      no_of_comparisons+=1
      arr1[j + 1] = key
  total_Times_row_Repeated +=1
  # no_of_comparisons += 1
  return arr1 , total_Times_row_Repeated, no_of_comparisons,no_of_exchangers


def selectionSort(arr):
    total_Times_row_Repeated = 0
    no_of_exchangers = 0
    no_of_comparisons = 0
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        total_Times_row_Repeated+=2
        # no_of_comparisons+=1
        for j in range(i + 1, len(arr)):

            if arr[min_idx] > arr[j]:
                min_idx = j
                # no_of_comparisons+=2
                no_of_comparisons += 1
                total_Times_row_Repeated+=3
            else:
                # no_of_comparisons+=2
                total_Times_row_Repeated+=2

                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        total_Times_row_Repeated+=2
        no_of_exchangers+=2
    total_Times_row_Repeated+=1
    # no_of_comparisons+=1
    return arr, total_Times_row_Repeated,no_of_comparisons, no_of_exchangers


def bubbleSort(arr):
    total_Times_row_Repeated = 0
    no_of_exchangers = 0
    no_of_comparisons = 0
    n = len(arr)
    total_Times_row_Repeated+=1

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                total_Times_row_Repeated+=5
                # no_of_comparisons+=3
                no_of_comparisons += 2
                no_of_exchangers+=2
            else:
                # no_of_comparisons+=3
                no_of_comparisons += 1
                total_Times_row_Repeated+=3
        # no_of_comparisons+=1
        total_Times_row_Repeated+=1
    # no_of_comparisons+=1
    total_Times_row_Repeated+=1
    return arr, total_Times_row_Repeated, no_of_comparisons, no_of_exchangers


def merge(arr, l, m, r):
    global total_Times_row_Repeated, no_of_comparisons, no_of_exchangers
    # total_Times_row_Repeated=t
    # no_of_comparisons=c
    # no_of_exchangers=e
    # print(total_Times_row_Repeated)
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    left = [0] * (n1)
    right = [0] * (n2)
    total_Times_row_Repeated +=4
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        left[i] = arr[l + i]
        total_Times_row_Repeated+=2
        # no_of_comparisons+=1
        no_of_exchangers+=1
    total_Times_row_Repeated+=1
    # no_of_comparisons+=1

    for j in range(0, n2):
        right[j] = arr[m + 1 + j]
        total_Times_row_Repeated += 2
        # no_of_comparisons += 1
        no_of_exchangers += 1
    total_Times_row_Repeated += 1
    # no_of_comparisons += 1

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    total_Times_row_Repeated+=3
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            total_Times_row_Repeated+=4
            no_of_exchangers+=1
            no_of_comparisons+=2
        else:
            arr[k] = right[j]
            j += 1
            total_Times_row_Repeated+=4
            no_of_comparisons+=2
            no_of_exchangers+=1
        k += 1
        total_Times_row_Repeated+=1
    total_Times_row_Repeated+=1
    no_of_comparisons+=1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
        total_Times_row_Repeated+=4
        no_of_exchangers+=1
        no_of_comparisons+=1
    no_of_comparisons+=1
    total_Times_row_Repeated+=1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
        total_Times_row_Repeated += 4
        no_of_exchangers += 1
        no_of_comparisons += 1
    no_of_comparisons += 1
    total_Times_row_Repeated += 1
    return total_Times_row_Repeated, no_of_comparisons,no_of_exchangers


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    global total_Times_row_Repeated, no_of_comparisons, no_of_exchangers
    total_Times_row_Repeated = 0
    no_of_exchangers = 0
    no_of_comparisons = 0
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        total_Times_row_Repeated+=5
        no_of_comparisons+=1
    else:
      no_of_comparisons+=1
      total_Times_row_Repeated+=1
    return arr, total_Times_row_Repeated, no_of_comparisons,no_of_exchangers
def randomPlotting(random):
    lengthx = []
    bubbleValues = []
    insertionValues = []
    selectionValues = []
    mergeValues = []
    # [[length,bubble,insertion,selection,merge][length,bubble,insertion,selection,merge]]
    for i in range(len(random)):
        lengthx.append(random[i][0])
        bubbleValues.append(random[i][1])
        insertionValues.append(random[i][2])
        selectionValues.append(random[i][3])
        mergeValues.append(random[i][4])
    plt.plot(lengthx, bubbleValues)
    plt.plot(lengthx, insertionValues)
    plt.plot(lengthx, selectionValues)
    plt.plot(lengthx, mergeValues)
    plt.title('Random order Graph')
    plt.xlabel('number of elements')
    # plt.ylabel('number of Comparison')
    # plt.ylabel('number of Repeats')
    plt.ylabel('number of Exchange')
    plt.legend(['bubble', 'insertion', 'selection', 'merge'])
    plt.xticks(lengthx)
    plt.show()
def increasingPlotting(increasing):
    lengthx = []
    bubbleValues = []
    insertionValues = []
    selectionValues = []
    mergeValues = []
    # [[length,bubble,insertion,selection,merge][length,bubble,insertion,selection,merge]]
    for i in range(len(increasing)):
        lengthx.append(increasing[i][0])
        bubbleValues.append(increasing[i][1])
        insertionValues.append(increasing[i][2])
        selectionValues.append(increasing[i][3])
        mergeValues.append(increasing[i][4])
    plt.plot(lengthx, bubbleValues)
    plt.plot(lengthx, insertionValues)
    plt.plot(lengthx, selectionValues)
    plt.plot(lengthx, mergeValues)
    plt.title('Increasing order Graph')
    plt.xlabel('number of elements')
    # plt.ylabel('number of Comparison')
    # plt.ylabel('number of Repeats')
    plt.ylabel('number of Exchange')
    plt.legend(['bubble', 'insertion', 'selection', 'merge'])
    plt.xticks(lengthx)
    plt.show()
def decreasingPlotting (decreasing):
    lengthx = []
    bubbleValues = []
    insertionValues = []
    selectionValues = []
    mergeValues = []
    # [[length,bubble,insertion,selection,merge][length,bubble,insertion,selection,merge]]
    for i in range(len(decreasing)):
        lengthx.append(decreasing[i][0])
        bubbleValues.append(decreasing[i][1])
        insertionValues.append(decreasing[i][2])
        selectionValues.append(decreasing[i][3])
        mergeValues.append(decreasing[i][4])
    plt.plot(lengthx, bubbleValues)
    plt.plot(lengthx, insertionValues)
    plt.plot(lengthx, selectionValues)
    plt.plot(lengthx, mergeValues)
    plt.title('Decreasing order Graph')
    plt.xlabel('number of elements')
    # plt.ylabel('number of Comparison')
    # plt.ylabel('number of Repeats')
    plt.ylabel('number of Exchange')
    plt.legend(['bubble', 'insertion', 'selection', 'merge'])
    plt.xticks(lengthx)
    plt.show()
def plotting (random,increasing,decreasing):
    randomPlotting(random)
    increasingPlotting(increasing)
    decreasingPlotting(decreasing)


def randomOrder(num1,num):
    arr=[]
    for i in range(0, num1):
        arr.append((i * 2) + 1)
    arr2 = randomize(arr).copy()
    arr3 = arr2.copy()
    arr4 = arr3.copy()
    arr5 = arr4.copy()
    print("\n Number of Hire:", hiring(arr5), "\n")
    print("\n---------------------\n\n Randomized order array: ",arr5 ,"\n Length of array: ",len(arr5),"\n")
    # print("\n", "For Randomized array: \n")
    insertionData = insertionSort(arr2)
    print("   Insertion sort:", insertionData[0], " total repeat :", insertionData[1], " Number of comparisons: ",insertionData[2], " Number of exchange: ", insertionData[3])
    # print(bubbleSort(arr3))
    bubbleData = bubbleSort(arr3)
    print("   Bubble    sort:", bubbleData[0], " total repeat :", bubbleData[1], " Number of comparisons: ",bubbleData[2], " Number of exchange: ", bubbleData[3])
    # print(selectionSort(arr4))
    selectionData = selectionSort(arr4)
    print("   Selection sort:", selectionData[0], " total repeat :", selectionData[1], " Number of comparisons: ",selectionData[2], " Number of exchange: ", selectionData[3])
    # print(mergeSort(arr5,0,len(arr5)-1))
    mergeData = mergeSort(arr5, 0, len(arr5) - 1)
    print("   Merge     sort:", mergeData[0], " total repeat :", mergeData[1], " Number of comparisons: ", mergeData[2]," Number of exchange: ", mergeData[3])
    # plotting(len(arr5), bubbleData[1], insertionData[1], selectionData[1], mergeData[1])
    return [num1,bubbleData[num],insertionData[num],selectionData[num],mergeData[num]]

def increasingOrder(num1,num):
    increasingOrder = []
    for i in range(0, num1):
        increasingOrder.append((i * 2) + 1)
    # print("\n For Increasing order: \n")
    increasingOrderArr2 = increasingOrder.copy()
    increasingOrderArr3 = increasingOrderArr2.copy()
    increasingOrderArr4 = increasingOrderArr3.copy()
    increasingOrderArr5 = increasingOrderArr4.copy()
    print("\n Increasing order array: ",increasingOrderArr5 ,"\n Length of array: ",len(increasingOrderArr5),"\n")
    increasingInsertionData = insertionSort(increasingOrderArr2)
    print("   Insertion sort:", increasingInsertionData[0], " total repeat :", increasingInsertionData[1]," Number of comparisons: ", increasingInsertionData[2], " Number of exchange: ", increasingInsertionData[3])

    increasingBubbleData = bubbleSort(increasingOrderArr3)
    print("   Bubble    sort:", increasingBubbleData[0], " total repeat :", increasingBubbleData[1], " Number of comparisons: ", increasingBubbleData[2], " Number of exchange: ", increasingBubbleData[3])

    increasingSelectionData = selectionSort(increasingOrderArr4)
    print("   Selection sort:", increasingSelectionData[0], " total repeat :", increasingSelectionData[1]," Number of comparisons: ", increasingSelectionData[2], " Number of exchange: ", increasingSelectionData[3])

    increasingMergeData = mergeSort(increasingOrderArr5, 0, len(increasingOrderArr5) - 1)
    print("   Merge     sort:", increasingMergeData[0], " total repeat :", increasingMergeData[1]," Number of comparisons: ", increasingMergeData[2], " Number of exchange: ", increasingMergeData[3])
    # plotting(len(increasingOrderArr5), increasingBubbleData[1], increasingInsertionData[1], increasingSelectionData[1],increasingMergeData[1])
    return [num1,increasingBubbleData[num],increasingInsertionData[num],increasingSelectionData[num],increasingMergeData[num]]
def decreasingOrder(num1,num):
    decreasingOrder = []
    for j in range(num1 - 1, -1, -1):
        decreasingOrder.append((j * 2) + 1)
    # print("\n For Decreasing order: \n")
    decreasingOrderArr2 = decreasingOrder.copy()
    decreasingOrderArr3 = decreasingOrderArr2.copy()
    decreasingOrderArr4 = decreasingOrderArr3.copy()
    decreasingOrderArr5 = decreasingOrderArr4.copy()
    print("\n Decreasing order array: ", decreasingOrderArr5, "\n Length of array: ",len(decreasingOrderArr5),"\n")
    decreasingInsertionData = insertionSort(decreasingOrderArr2)
    print("   Insertion sort:", decreasingInsertionData[0], " total repeat :", decreasingInsertionData[1]," Number of comparisons: ", decreasingInsertionData[2], " Number of exchange: ", decreasingInsertionData[3])

    decreasingBubbleData = bubbleSort(decreasingOrderArr3)
    print("   Bubble    sort:", decreasingBubbleData[0], " total repeat :", decreasingBubbleData[1]," Number of comparisons: ", decreasingBubbleData[2], " Number of exchange: ", decreasingBubbleData[3])

    decreasingSelectionData = selectionSort(decreasingOrderArr4)
    print("   Selection sort:", decreasingSelectionData[0], " total repeat :", decreasingSelectionData[1]," Number of comparisons: ", decreasingSelectionData[2], " Number of exchange: ", decreasingSelectionData[3])

    decreasingMergeData = mergeSort(decreasingOrderArr5, 0, len(decreasingOrderArr5) - 1)
    print("   Merge     sort:", decreasingMergeData[0], " total repeat :", decreasingMergeData[1]," Number of comparisons: ", decreasingMergeData[2], " Number of exchange: ", decreasingMergeData[3])
    # plotting(len(decreasingOrderArr5), decreasingBubbleData[1], decreasingInsertionData[1], decreasingSelectionData[1], decreasingMergeData[1])
    return [num1,decreasingBubbleData[num],decreasingInsertionData[num],decreasingSelectionData[num],decreasingMergeData[num]]

randomList=[]
increasingList=[]
decreasingList=[]
# for i in range(0, 1001,+100):
#     randomList.append(randomOrder(i,3))
#     increasingList.append(increasingOrder(i,3))
#     decreasingList.append(decreasingOrder(i,3))
# plotting(randomList,increasingList,decreasingList)
# print(randomList[0])
randomList.append(randomOrder(100,1))


# increasingList.append(increasingOrder(100,1))
# decreasingList.append(decreasingOrder(100,1))

# randomList.append(randomOrder(10, 1))
# increasingList.append(increasingOrder(10, 1))
# decreasingList.append(decreasingOrder(10, 1))
# # print(decreasingOrder)
# arr1=increasingOrder.copy()
# print("Ordered List:", arr1)
# print("Number of Hire:", hiring(arr1), "\n")
# print("Randomized List:", arr2)
#
# print("Number of Hire:", hiring(arr1))




