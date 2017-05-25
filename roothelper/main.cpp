/*****************************************************************************
 *
 * Created: 2016-2017 by Eetu Kahelin / eekkelund
 *
 * Copyright 2016-2017 Eetu Kahelin. All rights reserved.
 *
 * This file may be distributed under the terms of GNU Public License version
 * 3 (GPL v3) as defined by the Free Software Foundation (FSF). A copy of the
 * license should have been included with this file, or the project in which
 * this file belongs to. You may also find the details of GPL v3 at:
 * http://www.gnu.org/licenses/gpl-3.0.txt
 *
 * If you have any questions regarding the use of this file, feel free to
 * contact the author of this file, or the owner of the project in which
 * this file belongs to.
*****************************************************************************/
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    if (setuid(0)) {
        perror("setuid");
        return 1;
    }
        argv[0] = "/usr/bin/harbour-tide-editor";
        execv(argv[0], argv);

    return 0;
}
