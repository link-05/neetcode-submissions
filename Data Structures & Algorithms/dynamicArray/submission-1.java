class DynamicArray {
    private int[] arr;
    private int index = 0;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(index == arr.length) {
            resize();
        }
        arr[index] = n;
        index++;
    }

    public int popback() {
        index--;
        return arr[index];
    }

    private void resize() {
        int[] newArr = new int[arr.length * 2];
        for(int i = 0; i < index; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    public int getSize() {
        return index;
    }

    public int getCapacity() {
        return arr.length;
    }
}
