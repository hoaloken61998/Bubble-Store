class ValidateVarsClass:
    @staticmethod
    def validate_list(inde_list, de_list):
        # must select enough inde vars
        if not inde_list:
            print("Error: You must select at least one independent variable!")
            return False

        # must select one and only one de vars
        if not de_list:
            print("Error: You must select one dependent variable!")
            return False

        if len(de_list) > 1:
            print("Error: You can only select one dependent variable!")
            return False

        overlap_cols = set(inde_list) & set(de_list)
        if overlap_cols:
            print("Error: Independent variables must be different from dependent ones!", overlap_cols)
            return False

        return True


