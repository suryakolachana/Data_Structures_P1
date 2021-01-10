class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
         return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

sub_child_user2 = "surya"
sub_child.add_user(sub_child_user2)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        if len(group.get_groups()) == 0:
            return False
        for i in group.get_groups():
            if is_user_in_group(user,i):
                return True
    return False

def main():
    print(is_user_in_group("sub_child_user", parent))   # True

    print(is_user_in_group("surya", parent))   # True
    
    print(is_user_in_group("parent", parent))  # False

    print(is_user_in_group("child", parent))  # False

    print(is_user_in_group("child", child))  # False
    
    #EDGE CASES:

    print(is_user_in_group("", parent))  # False

    print(is_user_in_group("", child))  # False

if __name__ == "__main__":
    main()


