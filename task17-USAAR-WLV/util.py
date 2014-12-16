#!/usr/bin/env python -*- coding: utf-8 -*-

def per_section(it):
  """ Read a file and yield sections using empty line as delimiter """
  section = []
  for line in it:
    if line.strip():
      section.append(line)
    else:
      yield ''.join(section)
      section = []
  # yield any remaining lines as a section too
  if section:
    yield ''.join(section)