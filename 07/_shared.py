from collections import Counter


def get_directory_sizes(puzzle_input: str) -> Counter[str]:
    """Parses the given puzzle input and returns the sizes of each directory.

    Parameters
    ----------
    puzzle_input: :class:`str`
        The puzzle input containing the commands run.

    Returns
    -------
    :class:`collections.Counter`
        A counter containing a mapping of the directories and their sizes.
    """
    lines = puzzle_input.splitlines()

    counts = Counter()
    current_path = []

    for line in lines:
        line = line.lstrip("$ ")

        if line.startswith("cd"):
            command, _, selected_folder = line.partition(" ")

            if selected_folder == "/":
                current_path.clear()
            elif selected_folder == "..":
                if current_path:
                    current_path.pop()
            else:
                current_path.append(selected_folder)

            continue

        if not line.startswith(("dir", "ls")):
            filesize_str, _, _ = line.partition(" ")
            filesize = int(filesize_str)

            counts["/" + "/".join(current_path)] += filesize

            for i in range(len(current_path)):
                counts["/" + "/".join(current_path[:i])] += filesize

    return counts
