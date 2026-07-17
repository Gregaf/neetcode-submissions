/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
        const stack = [[p, q]];
        
        while (stack.length > 0) {
            const [rootOne, rootTwo] = stack.pop();

            if (!rootOne && !rootTwo) continue;
            if (!rootOne || !rootTwo || rootOne.val !== rootTwo.val) {
                return false;
            }

            stack.push([rootOne.left, rootTwo.left]);
            stack.push([rootOne.right, rootTwo.right]);
        }

        return true;
    }
}
