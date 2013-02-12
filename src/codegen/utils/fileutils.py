#
# Copyright (c) 2012 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

class FileUtils(object):
    '''
    Provides File/Directory related services
    '''

    LINE_SEPARATOR = "line.separator";
    ENCODING = "UTF-8";
    NEW_LINE = '\n'

    @staticmethod
    def deleteAll(directoryPath):
        '''
        Deletes all files in given directoryPath
        
        @param directoryPath
                   directory to clean        
        '''
        for the_file in os.listdir(directoryPath):
            file_path = os.path.join(directoryPath, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    @staticmethod
    def delete(filePath):
        '''
        Deletes given file
        
        @param filePath
                   file to delete
        
        @return boolean
        '''
        if os.path.isfile(filePath):
            os.unlink(filePath)

    @staticmethod
    def rename(filePath, newName):
        '''
        Renames file
        
        @param filePath
                   File to rename
        @param newName
                   new file name
        '''
        newfile = filePath.split(os.pathsep)
        newfile[-1] = newName
        return os.rename(filePath, os.pathsep.join(newfile))

    @staticmethod
    def list(directoryPath):
        '''
        List all files in given directory
        
        @param directoryPath
        
        @return Files
        '''
        return os.listdir(directoryPath)

    @staticmethod
    def getContent(path, appendNewLine=False):
        '''
        Reads file content
        
        @param path
                   file path to read from
        @param appendNewLine
                   append new line to the end of the file
        
        @return file content
        '''
        with open(path) as f:
            file_content = f.read()

        return file_content if not appendNewLine else (file_content + FileUtils.NEW_LINE)

    @staticmethod
    def getContentAsList(path):
        '''
        Reads file content

        @return file content as list of strings
        '''
        return [line for line in open(path)]

    @staticmethod
    def save(filePath, content):
        '''
        Stores file

        @param filePath
                   file path
        @param content
                   file content
        '''
        try:
            f = open(filePath, 'w')
            f.write(content)
            f.flush()
        finally:
            if f and not f.closed:
                f.close()
