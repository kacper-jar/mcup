from mcup import __version__

from mcup.cli.language import Language


class AboutCommand:
    @staticmethod
    def run(args):
        language = Language()

        art = """
::::    ::::   ::::::::  :::    ::: :::::::::
+:+:+: :+:+:+ :+:    :+: :+:    :+: :+:    :+:
+:+ +:+:+ +:+ +:+        +:+    +:+ +:+    +:+
+#+  +:+  +#+ +#+        +#+    +:+ +#++:++#+
+#+       +#+ +#+        +#+    +#+ +#+
#+#       #+# #+#    #+# #+#    #+# #+#
###       ###  ########   ########  ###
"""

        print(art)
        print(language.get_string("ABOUT_TITLE", __version__))
        print(language.get_string("ABOUT_DESCRIPTION"))
        print(language.get_string("ABOUT_LICENSE"))
        print(language.get_string("ABOUT_SOURCE_CODE"))
        print(language.get_string("ABOUT_ISSUES"))
