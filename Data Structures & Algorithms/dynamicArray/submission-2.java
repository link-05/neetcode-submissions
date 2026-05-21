class DynamicArray {
    private int[] arr;
    private int index = 0;
    private int capacity;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        arr = new int[capacity];
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(index == capacity) {
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
        capacity *= 2;
        int[] newArr = new int[capacity];
        for(int i = 0; i < index; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    public int getSize() {
        return index;
    }

    public int getCapacity() {
        return capacity;
    }
}
