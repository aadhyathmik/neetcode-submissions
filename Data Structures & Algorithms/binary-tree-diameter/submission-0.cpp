class Solution {
public:
    int res = 0;
    int height(TreeNode* node) {
        if (!node) return 0;
        int left = height(node->left);
        int right = height(node->right);
        res = max(res, left + right);
        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return res;
    }
};