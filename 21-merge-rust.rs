// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}
struct Solution;
impl Solution {
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // let mut dummy = ListNode::new(0);
        // let mut cur : * Option<Box<ListNode>> = &mut dummy.next;

        // while let (Some(l1), Some(l2)) = (list1, list2) {
        //     if list1.value < list2.value {
        //         cur.next = list1;
        //         list1 = cur.next.next;
        //     } else {
        //         cur.next = list2;
        //     }
        // }


        // dummy.next

        let Some(mut l1) = list1 else {
            return list2;
        };
        let Some(mut l2) = list2 else {
            return list1;
        };

        if l2.val > l1.val {
            l1.next = Self::merge_two_lists(l1.next, Some(l2));
            return Some(l1);
        } else {
            l2.next = Self::merge_two_lists(l2.next, Some(l1));
            return Some(l2);
        }
    }
}

fn main() {
    let list1 = ListNode {
        val: 1,
        next : Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode {
                val: 4,
                next: None,
            }))
        }))
    };
    let list2 = ListNode {
        val: 1,
        next : Some(Box::new(ListNode {
            val: 3,
            next: Some(Box::new(ListNode {
                val: 4,
                next: None,
            }))
        }))
    };
    dbg!(list1.clone());
    dbg!(list2.clone());
    let list = Solution::merge_two_lists(Some(Box::new(list1)), Some(Box::new(list2)));
    dbg!(list);
}