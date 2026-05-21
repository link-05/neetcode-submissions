class LinkedList {
    class Node {
        Node next = null;
        int value;
        public Node(int value) {
            this.value = value;
        }
    }
    Node head;
    Node tail;
    public LinkedList() {
        head = null;
        tail = head;
    }

    public int get(int index) {
        Node curr = head;
        while(curr != null) {
            if(index != 0) {
                index--;
                curr = curr.next;
            } else {
                return curr.value;
            }
        }
        return -1;
    }

    public void insertHead(int val) {
        Node newHead = new Node(val);
        if(head != null) {
            newHead.next = head;
            head = newHead;
        } else {
            head = newHead;
            tail = newHead;
        }
    }

    public void insertTail(int val) {
        if(head == null) {
            head = new Node(val);
            tail = head;
            return;
        }
        tail.next = new Node(val);
        tail = tail.next;
    }

    public boolean remove(int index) {
        if(head == null) return false;
        if(index == 0) {
            head = head.next;
            return true;
        }
        Node curr = head;
        while(curr.next != null) {
            if(index != 1) {
                index--;
                curr = curr.next;
            } else {
                curr.next = curr.next.next;
                if(curr.next == null) {
                    tail = curr;
                }
                return true;
            }
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> ret = new ArrayList<>();
        Node curr = head;
        while(curr != null) {
            ret.add(curr.value);
            curr = curr.next;
        }
        return ret;
    }
}
