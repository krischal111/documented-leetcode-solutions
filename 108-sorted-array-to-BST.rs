// # Definition for a binary tree node.
// # class TreeNode:
// #     def __init__(self, val=0, left=None, right=None):
// #         self.val = val
// #         self.left = left
// #         self.right = right

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }

// struct Solution;
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let l = nums.len();
        if l == 0 {
            return None;
        }
        let mid = l/2;
        Some(Rc::new(RefCell::new(TreeNode {
            val: nums[mid],
            left: Self::sorted_array_to_bst(nums[..mid].to_vec()),
            right: Self::sorted_array_to_bst(nums[mid+1..].to_vec())
        })))
    }
}

// fn main() {
//     let l = vec![-10, -3, 0, 5, 9];
//     let answer = Solution::sorted_array_to_bst(l);
//     dbg!(answer);
// }

// class Solution:
// def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
//         l = len(nums)
//         if not l:
//             return None
//         mid = l//2
//         return TreeNode(nums[mid], left=self.sortedArrayToBST(nums[:mid]), right=self.sortedArrayToBST(nums[mid+1:]))

        
