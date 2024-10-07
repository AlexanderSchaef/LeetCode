
public class ListNode {
int val;
ListNode next;
ListNode() {}
ListNode(int val) { this.val = val; }
ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum = 0;
        int place = 1;
        while (l1.next != null) {
            sum += l1.val * place;
            l1 = l1.next;
            place *= 10;
        }
        sum += l1.val * place;

        place = 1;
        while (l2.next != null) {
            sum += l2.val * place;
            l2 = l2.next;
            place *= 10;
        }
        sum += l2.val * place;

        // the correct sum has been achieved
        // Will now store in new linked list

        place = 10; // will now be used as divisor
        int count = 0;

        int num = 10;
        if (sum >= num) {
            while (sum >= num) {
                num = num * 10;
                count++;
            }
        }
        // num = power of 10 greater than or equal to the value
        // count = how many positions the new ListNode will need in storage

        ListNode[] solutionParts = new ListNode[count + 1];

        int i = 0;
        int position = 0;
        if (sum == 0) {
            return new ListNode(0);
        } else {
            while (sum != 0) {
                position = sum % 10;
                sum = (sum - position) / 10;
                solutionParts[i] = new ListNode(position);
                i++;
            }
        }

        // write the answer into one list node
        ListNode solution = new ListNode(0);
        
        solution.val = solutionParts[0].val;
        for (int j = solutionParts.length; j > 0; j--) {
            solution.val = solutionParts[j - 1].val;
            if (j != 1) {
                solution = new ListNode(-1, solution);
            } else {
                solution.val = solutionParts[j - 1].val;
            }

        }
        return solution;

    }
}