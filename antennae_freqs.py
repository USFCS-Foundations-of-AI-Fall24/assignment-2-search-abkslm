from ortools.sat.python import cp_model


def frequency_finder():
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    freqs = {0 :'f1', 1:'f2', 2:'f3'}

    Antenna1 = model.NewIntVar(0, 2, "A1")
    Antenna2 = model.NewIntVar(0, 2, "A2")
    Antenna3 = model.NewIntVar(0, 2, "A3")
    Antenna4 = model.NewIntVar(0, 2, "A4")
    Antenna5 = model.NewIntVar(0, 2, "A5")
    Antenna6 = model.NewIntVar(0, 2, "A6")
    Antenna7 = model.NewIntVar(0, 2, "A7")
    Antenna8 = model.NewIntVar(0, 2, "A8")
    Antenna9 = model.NewIntVar(0, 2, "A9")

    model.Add(Antenna1 != Antenna2)
    model.Add(Antenna1 != Antenna3)
    model.Add(Antenna2 != Antenna4)
    model.Add(Antenna2 != Antenna3)
    model.Add(Antenna2 != Antenna5)
    model.Add(Antenna2 != Antenna6)
    model.Add(Antenna3 != Antenna6)
    model.Add(Antenna3 != Antenna9)
    model.Add(Antenna4 != Antenna5)
    model.Add(Antenna5 != Antenna2)
    model.Add(Antenna6 != Antenna7)
    model.Add(Antenna6 != Antenna8)
    model.Add(Antenna7 != Antenna8)
    model.Add(Antenna8 != Antenna9)
    model.Add(Antenna9 != Antenna3)

    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Antenna 1: {freqs[solver.Value(Antenna1)]}")
        print(f"Antenna 2: {freqs[solver.Value(Antenna2)]}")
        print(f"Antenna 3: {freqs[solver.Value(Antenna3)]}")
        print(f"Antenna 4: {freqs[solver.Value(Antenna4)]}")
        print(f"Antenna 5: {freqs[solver.Value(Antenna5)]}")
        print(f"Antenna 6: {freqs[solver.Value(Antenna6)]}")
        print(f"Antenna 7: {freqs[solver.Value(Antenna7)]}")
        print(f"Antenna 8: {freqs[solver.Value(Antenna8)]}")
        print(f"Antenna 9: {freqs[solver.Value(Antenna9)]}")
    else:
        print("No solution found.")

def main():
    frequency_finder()

if __name__ == '__main__':
    main()