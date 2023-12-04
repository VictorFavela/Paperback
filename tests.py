"""Tests"""
import unittest

from word_tree import WordTree, load_word_tree

VALID_N5 = {
    "often",
    "typed",
    "queue",
    "quite",
    "codes",
    "hurry",
    "kills",
    "alive",
    "bears",
    "stays",
    "tanks",
    "token",
    "great",
    "hopes",
    "tells",
    "kinds",
    "earth",
    "lucky",
    "dozen",
    "shuts",
    "class",
    "fewer",
    "claim",
    "tapes",
    "close",
    "agree",
    "known",
    "lying",
    "score",
    "funds",
    "cease",
    "lifes",
    "fully",
    "cross",
    "marks",
    "hello",
    "hoped",
    "links",
    "dirty",
    "lower",
    "state",
    "rapid",
    "chars",
    "force",
    "moved",
    "stone",
    "crisp",
    "picks",
    "tight",
    "sells",
    "phase",
    "spend",
    "trash",
    "taste",
    "truck",
    "month",
    "spoke",
    "hours",
    "noise",
    "heads",
    "chaos",
    "bases",
    "copys",
    "based",
    "split",
    "flies",
    "taken",
    "magic",
    "minds",
    "sleep",
    "thing",
    "calls",
    "faith",
    "keeps",
    "parts",
    "third",
    "joins",
    "which",
    "total",
    "power",
    "sales",
    "noisy",
    "foots",
    "messy",
    "abuse",
    "stuck",
    "ought",
    "tying",
    "issue",
    "drive",
    "learn",
    "valid",
    "being",
    "silly",
    "judge",
    "borne",
    "order",
    "grown",
    "those",
    "empty",
    "teeth",
    "payed",
    "marry",
    "using",
    "sides",
    "leafs",
    "limit",
    "vital",
    "extra",
    "spent",
    "votes",
    "party",
    "seems",
    "upper",
    "forms",
    "gives",
    "worth",
    "first",
    "aware",
    "backs",
    "short",
    "shows",
    "march",
    "awful",
    "brown",
    "fills",
    "three",
    "reads",
    "began",
    "speak",
    "teach",
    "leach",
    "wheel",
    "dates",
    "prone",
    "award",
    "image",
    "piece",
    "solid",
    "green",
    "cheap",
    "spell",
    "under",
    "hence",
    "drink",
    "wills",
    "moves",
    "enemy",
    "enter",
    "named",
    "comes",
    "music",
    "sadly",
    "stood",
    "habit",
    "water",
    "clock",
    "doubt",
    "serve",
    "track",
    "court",
    "lines",
    "walks",
    "naive",
    "chain",
    "worry",
    "meets",
    "hears",
    "doing",
    "truly",
    "black",
    "stage",
    "inchs",
    "truth",
    "alone",
    "rough",
    "topic",
    "heart",
    "grind",
    "owner",
    "ready",
    "seeks",
    "knows",
    "sound",
    "means",
    "saves",
    "since",
    "clear",
    "asked",
    "would",
    "shift",
    "thats",
    "liked",
    "rules",
    "ditto",
    "shops",
    "steal",
    "offer",
    "joint",
    "upset",
    "sends",
    "skill",
    "lands",
    "safer",
    "place",
    "enjoy",
    "pause",
    "sense",
    "bound",
    "edits",
    "lived",
    "grant",
    "while",
    "input",
    "death",
    "needs",
    "touch",
    "fries",
    "falls",
    "house",
    "begin",
    "folks",
    "write",
    "small",
    "datum",
    "posts",
    "merit",
    "trial",
    "worst",
    "owing",
    "human",
    "books",
    "users",
    "takes",
    "feeds",
    "share",
    "talks",
    "exact",
    "could",
    "prior",
    "mixed",
    "route",
    "costs",
    "weird",
    "daily",
    "logic",
    "chair",
    "level",
    "trunk",
    "stops",
    "works",
    "print",
    "catch",
    "aside",
    "shown",
    "table",
    "drawn",
    "react",
    "apply",
    "still",
    "round",
    "album",
    "break",
    "usage",
    "badly",
    "begun",
    "right",
    "waits",
    "broke",
    "holes",
    "reply",
    "count",
    "trace",
    "fresh",
    "exist",
    "flied",
    "ahead",
    "night",
    "treat",
    "brief",
    "watch",
    "least",
    "tried",
    "value",
    "mouth",
    "staff",
    "binds",
    "hangs",
    "saved",
    "speed",
    "voice",
    "sheet",
    "blame",
    "story",
    "helps",
    "label",
    "mixes",
    "angle",
    "drove",
    "quick",
    "delay",
    "fails",
    "units",
    "board",
    "clean",
    "shell",
    "ended",
    "there",
    "items",
    "build",
    "north",
    "wrong",
    "basic",
    "model",
    "trees",
    "signs",
    "women",
    "lists",
    "wears",
    "awake",
    "river",
    "lives",
    "shall",
    "whole",
    "refer",
    "tooth",
    "flown",
    "raise",
    "games",
    "locks",
    "traps",
    "areas",
    "occur",
    "miles",
    "press",
    "shoot",
    "video",
    "patch",
    "heard",
    "spite",
    "plain",
    "threw",
    "admit",
    "gains",
    "found",
    "aimed",
    "boxes",
    "graph",
    "about",
    "fixed",
    "reach",
    "acted",
    "pairs",
    "deads",
    "train",
    "plots",
    "scene",
    "rates",
    "stand",
    "given",
    "solve",
    "feels",
    "dream",
    "leave",
    "handy",
    "vague",
    "large",
    "scrap",
    "proof",
    "sorts",
    "unite",
    "finds",
    "fatal",
    "arise",
    "scale",
    "dying",
    "nasty",
    "check",
    "start",
    "wider",
    "white",
    "guess",
    "rooms",
    "words",
    "light",
    "trust",
    "early",
    "floor",
    "types",
    "moral",
    "discs",
    "adopt",
    "spare",
    "until",
    "quote",
    "sight",
    "wrote",
    "every",
    "nicer",
    "omits",
    "cause",
    "crazy",
    "legal",
    "world",
    "thank",
    "smile",
    "front",
    "avoid",
    "point",
    "alarm",
    "usual",
    "woman",
    "young",
    "store",
    "glass",
    "hands",
    "suits",
    "holds",
    "cases",
    "metal",
    "sites",
    "above",
    "fight",
    "hotel",
    "stick",
    "shape",
    "these",
    "group",
    "wants",
    "grand",
    "along",
    "false",
    "loose",
    "lunch",
    "files",
    "forth",
    "stuff",
    "dated",
    "outer",
    "funny",
    "style",
    "built",
    "shelf",
    "opens",
    "makes",
    "quits",
    "eaten",
    "fault",
    "cycle",
    "ladys",
    "added",
    "event",
    "might",
    "looks",
    "inner",
    "plane",
    "range",
    "whose",
    "grave",
    "cares",
    "block",
    "fancy",
    "argue",
    "plays",
    "crash",
    "never",
    "notes",
    "noted",
    "walls",
    "prove",
    "elect",
    "trick",
    "visit",
    "error",
    "sorry",
    "flash",
    "title",
    "grows",
    "alter",
    "equal",
    "pulls",
    "hides",
    "alias",
    "terms",
    "novel",
    "bodys",
    "below",
    "paper",
    "tasks",
    "putts",
    "space",
    "seven",
    "angry",
    "shame",
    "twice",
    "cards",
    "likes",
    "major",
    "match",
    "throw",
    "horse",
    "depth",
    "chips",
    "study",
    "facts",
    "waste",
    "timed",
    "years",
    "times",
    "money",
    "local",
    "goods",
    "apple",
    "brand",
    "worse",
    "happy",
    "turns",
    "plans",
    "imply",
    "index",
    "ideas",
    "carry",
    "loses",
    "quiet",
    "later",
    "south",
    "deems",
    "other",
    "float",
    "deals",
    "drops",
    "gross",
    "pound",
    "jumps",
    "plant",
    "sizes",
    "heavy",
    "tests",
    "annoy",
    "warns",
    "coded",
    "prime",
    "fishs",
    "older",
    "allow",
    "basis",
    "after",
    "evens",
    "think",
    "hints",
    "tries",
    "yours",
    "tends",
    "price",
    "lacks",
    "saint",
    "minor",
    "doors",
    "sugar",
    "stock",
    "lorry",
    "knock",
    "spots",
    "guard",
    "dealt",
    "field",
    "loads",
    "fixes",
    "guide",
    "phone",
    "draws",
    "amuse",
    "media",
    "cover",
    "views",
    "apart",
    "meant",
    "sharp",
    "lesss",
    "where",
    "peace",
    "movie",
    "bytes",
    "weeks",
    "blank",
    "names",
    "their",
    "final",
    "today",
    "radio",
    "eight",
    "leads",
    "chose",
    "maybe",
    "wishs",
    "digit",
    "going",
    "frame",
    "pages",
    "child",
    "entry",
    "again",
    "bring",
    "bites",
    "ideal",
    "lasts",
    "filed",
}

VALID_N4 = {
    "dies",
    "head",
    "save",
    "read",
    "pure",
    "roll",
    "fail",
    "path",
    "talk",
    "fact",
    "ours",
    "rule",
    "inch",
    "omit",
    "loan",
    "port",
    "very",
    "fair",
    "mere",
    "busy",
    "same",
    "seen",
    "what",
    "area",
    "disc",
    "town",
    "full",
    "hint",
    "clue",
    "need",
    "sold",
    "face",
    "fall",
    "live",
    "trys",
    "main",
    "bank",
    "film",
    "once",
    "post",
    "chip",
    "ball",
    "hold",
    "club",
    "seek",
    "flag",
    "info",
    "went",
    "hand",
    "pile",
    "runs",
    "bugs",
    "pair",
    "made",
    "item",
    "pint",
    "lied",
    "jobs",
    "race",
    "till",
    "life",
    "tied",
    "leaf",
    "pull",
    "have",
    "told",
    "cuts",
    "lost",
    "kept",
    "last",
    "long",
    "text",
    "fits",
    "play",
    "days",
    "harm",
    "role",
    "when",
    "part",
    "some",
    "fine",
    "plot",
    "real",
    "nice",
    "lock",
    "tell",
    "wall",
    "book",
    "type",
    "heat",
    "lazy",
    "root",
    "ones",
    "wild",
    "fill",
    "wind",
    "land",
    "safe",
    "putt",
    "side",
    "says",
    "drop",
    "room",
    "aims",
    "jump",
    "ease",
    "news",
    "plus",
    "warm",
    "like",
    "farm",
    "king",
    "west",
    "body",
    "does",
    "cent",
    "blue",
    "sort",
    "gave",
    "step",
    "gain",
    "shut",
    "easy",
    "wear",
    "mile",
    "base",
    "make",
    "city",
    "high",
    "mess",
    "year",
    "team",
    "grew",
    "link",
    "used",
    "note",
    "bids",
    "sure",
    "mine",
    "felt",
    "sell",
    "poem",
    "ship",
    "huge",
    "file",
    "list",
    "glad",
    "adds",
    "knew",
    "only",
    "sale",
    "folk",
    "next",
    "feet",
    "hate",
    "hope",
    "byte",
    "lead",
    "love",
    "they",
    "seem",
    "code",
    "take",
    "risk",
    "puts",
    "band",
    "door",
    "mans",
    "wide",
    "loop",
    "road",
    "unit",
    "whom",
    "hell",
    "meet",
    "view",
    "trap",
    "worn",
    "thin",
    "this",
    "fate",
    "plan",
    "wine",
    "with",
    "park",
    "lies",
    "food",
    "cums",
    "sake",
    "turn",
    "feed",
    "wash",
    "lose",
    "hall",
    "away",
    "wish",
    "date",
    "rain",
    "walk",
    "dare",
    "keys",
    "must",
    "tape",
    "rare",
    "joke",
    "than",
    "shop",
    "came",
    "dumb",
    "test",
    "keep",
    "buys",
    "neck",
    "hunt",
    "hang",
    "hits",
    "dear",
    "load",
    "lots",
    "find",
    "junk",
    "lend",
    "page",
    "push",
    "duty",
    "zero",
    "goes",
    "ride",
    "copy",
    "eats",
    "lack",
    "draw",
    "rise",
    "bits",
    "sign",
    "gets",
    "pick",
    "hide",
    "four",
    "paid",
    "open",
    "rate",
    "miss",
    "less",
    "hear",
    "vans",
    "lain",
    "host",
    "each",
    "work",
    "edit",
    "sets",
    "disk",
    "cure",
    "self",
    "tank",
    "boat",
    "hole",
    "deep",
    "frys",
    "mind",
    "vote",
    "also",
    "plug",
    "hack",
    "keen",
    "fast",
    "ring",
    "mark",
    "half",
    "onto",
    "logs",
    "mass",
    "rely",
    "flys",
    "held",
    "rids",
    "were",
    "flow",
    "wore",
    "obey",
    "here",
    "fire",
    "soft",
    "fear",
    "pipe",
    "poet",
    "ages",
    "size",
    "show",
    "odds",
    "died",
    "from",
    "sits",
    "desk",
    "kind",
    "tend",
    "pays",
    "cost",
    "many",
    "bear",
    "able",
    "upon",
    "bore",
    "fell",
    "kill",
    "quit",
    "such",
    "pain",
    "bill",
    "ways",
    "call",
    "pass",
    "scan",
    "warn",
    "suit",
    "will",
    "boot",
    "char",
    "site",
    "game",
    "rest",
    "idea",
    "data",
    "tune",
    "look",
    "time",
    "laws",
    "owed",
    "even",
    "cell",
    "left",
    "hill",
    "eyes",
    "past",
    "join",
    "thus",
    "girl",
    "term",
    "took",
    "said",
    "deal",
    "else",
    "stay",
    "tree",
    "wise",
    "foot",
    "card",
    "hung",
    "well",
    "bets",
    "hair",
    "mode",
    "your",
    "cope",
    "ugly",
    "peak",
    "bury",
    "cold",
    "come",
    "into",
    "deem",
    "case",
    "done",
    "numb",
    "free",
    "pool",
    "user",
    "send",
    "dark",
    "move",
    "poll",
    "trip",
    "give",
    "word",
    "firm",
    "edge",
    "bars",
    "slow",
    "then",
    "loss",
    "mean",
    "fund",
    "name",
    "grow",
    "vary",
    "bulk",
    "form",
    "boxs",
    "lift",
    "ends",
    "nine",
    "ties",
    "feel",
    "stop",
    "late",
    "dump",
    "best",
    "back",
    "both",
    "sees",
    "fish",
    "plea",
    "dead",
    "rush",
    "home",
    "sent",
    "been",
    "blow",
    "east",
    "most",
    "none",
    "wins",
    "flew",
    "help",
    "hour",
    "more",
    "core",
    "soon",
    "uses",
    "want",
    "vice",
    "legs",
    "mail",
    "wire",
    "much",
    "hard",
    "army",
    "asks",
    "down",
    "bind",
    "drew",
    "them",
    "that",
    "owes",
    "bite",
    "acts",
    "near",
    "true",
    "spot",
    "wife",
    "flat",
    "good",
    "vast",
    "slip",
    "wait",
    "lady",
    "just",
    "wons",
    "task",
    "line",
    "over",
    "week",
    "gone",
    "lets",
    "poor",
    "luck",
    "care",
    "ever",
    "five",
    "know",
    "pack",
}


class WordTreeTestCases(unittest.TestCase):
    """Tests WordTree class"""

    def setUp(self) -> None:
        self.word_file = "english-words.10"

    def test_validn5(self):
        """Test WordTree generates all valid words of length 3"""
        word_tree = WordTree()
        load_word_tree(word_tree, self.word_file)

        bog = ["*", "*", "*", "*", "*"]

        valid_words = word_tree.get_all_valid_words(bog)

        valid_n5 = {word for word in valid_words if len(word) == 5}

        self.assertSetEqual(valid_n5, VALID_N5)

    def test_validn4(self):
        """Test WordTree generates all valid words of length 4"""
        word_tree = WordTree()
        load_word_tree(word_tree, self.word_file)

        bog = ["*", "*", "*", "*", "*"]

        valid_words = word_tree.get_all_valid_words(bog)

        valid_n4 = {word for word in valid_words if len(word) == 4}

        self.assertSetEqual(valid_n4, VALID_N4)


if __name__ == "__main__":
    unittest.main()