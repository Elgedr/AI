def simple_resolution_solver(KB, neg_alpha):
    todo = [neg_alpha]
    done = KB.copy()
    while todo:
        current = todo.pop()
        subsumption_check = True
        for clause in done + todo:
            if clause == current:
                subsumption_check = False
                break
        if subsumption_check is True:
            for clause in done:
                resolvents = resolve(current, clause)
                for resolvent in resolvents:
                    if not resolvent:
                        print("Proof is found. True")
                        return True
                    elif list(resolvent) not in todo:
                        todo.append(list(resolvent))
            done.append(current)
    print("Loop ended without proof. False")
    return False


def resolve(first_clause, second_clause):
    res = []
    for element in first_clause:
        first_clause_elements_list = first_clause.copy()
        second_clause_elements_list = second_clause.copy()
        if element.find("-") != -1:  # if element have a negation "-a"
            for element2 in second_clause:
                if element[1:] == element2:  # if clause is "a V -a" remove both
                    second_clause_elements_list.remove(element2)
                    first_clause_elements_list.remove(element)
                    computed_res = first_clause_elements_list + second_clause_elements_list
                    res.append(set(computed_res))  # leave only 1 occurrence of the elements
        for element2 in second_clause:
            if element2[1:] == element:
                first_clause_elements_list.remove(element)
                second_clause_elements_list.remove(element2)
                computed_res = first_clause_elements_list + second_clause_elements_list
                res.append(set(computed_res))
    return res


if __name__ == "__main__":
    knowledge_base = [
        ["-op", "w5"],
        ["-w3", "-s3", "w4"],
        ["op", "-w5"],
        ["-w5", "-cb1", "w3"],
        ["-w5", "-cb2", "w6"],
        ["-w0", "l1"],
        ["w0", "-l1"],
        ["-w6", "p2"],
        ["w6", "-p2"],
        ["-w3", "p1"],
        ["w3", "-p1"],
        ["-w4", "l2"],
        ["w4", "-l2"],
        ["-w2", "-s2", "-w0"],
        ["-w3", "-s1", "w1"],
        ["-w3", "s1", "w2"],
        ["-w1", "-s2", "w0"],
        ["-w2", "s2", "w0"],
    ]

    # First question
    KB1 = [["op"], ["cb2"]]
    neg_alpha1 = ["-p2"]
    print("First question resolving")
    simple_resolution_solver(knowledge_base + KB1, neg_alpha1)

    # Second question
    KB2 = [["op"], ["cb1"], ["-s1"], ["s2"]]
    neg_alpha2 = ["l1"]
    print(" ")
    print("Second question resolving")
    simple_resolution_solver(knowledge_base + KB2, neg_alpha2)

    # Third question
    KB3 = [["op"], ["-l1"], ["s1"], ["s2"]]
    neg_alpha3 = ["cb1"]
    print(" ")
    print("Third question resolving")
    simple_resolution_solver(knowledge_base + KB3, neg_alpha3)
