//
// Copyright (c) 2014 Red Hat, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

package org.ovirt.engine.sdk.generator.utils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

/**
 * Provides file/directory related services.
 */
public class FileUtils {
    /**
     * Deletes all files in given directory.
     */
    public static boolean deleteAllFiles(String directory) {
        boolean res = true;
        for (File f : list(directory)) {
            res = res & f.delete();
        }
        return res;
    }

    /**
     * List all files in given directory.
     */
    public static File[] list(String directory) {
        return new File(directory).listFiles();
    }

    /**
     * Stores file.
     *
     * @param path file path
     * @param content file content
     */
    public static void saveFile(String path, String content) {
        PrintWriter out = null;
        if (path != null && content != null) {
            try {
                out = new PrintWriter(path);
                out.println(content);
            }
            catch (FileNotFoundException e) {
                // TODO: Log error
                e.printStackTrace();
                throw new RuntimeException("File \"" + path + "\" write failed.");
            }
            finally {
                if (out != null) {
                    out.close();
                }
            }
        }
    }
}
