function array_without_zero(arr,element) //Defining function for array without zeros
{
 for(var i=0; i<arr.length;i++ ) // loop throuh array with array length
 {
    if(arr[i]==element) // check given element is equal to array of index element
        arr.splice(i,1); // splice is used to remove that indexed element in array 
 }
}
var data = [0, 1, 2, 'stop', 2, 0, 1, 'stop'] //Defining data array

array_without_zero(data,0) // calling function with data array and element 0
document.write(data); // used to disply array in html page as output.